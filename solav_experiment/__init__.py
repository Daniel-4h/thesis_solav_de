import random
from otree.api import *
from .lexicon import Lexicon
import itertools


def make_likert6(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6],
        label=label,
        widget=widgets.RadioSelect,
    )


class C(BaseConstants):
    NAME_IN_URL = 'solav_experiment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 4



class Subsession(BaseSubsession):
    pass
    

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Questions for Policy Area 1
    pol_evehic1 = make_likert6(Lexicon.vignettes["PolicyArea1"]["question1"])
    pol_evehic2 = make_likert6(Lexicon.vignettes["PolicyArea1"]["question2"])
    pol_evehic3 = make_likert6(Lexicon.vignettes["PolicyArea1"]["question3"])
    pol_evehic4 = make_likert6(Lexicon.vignettes["PolicyArea1"]["question4"])
    pol_evehic5 = make_likert6(Lexicon.vignettes["PolicyArea1"]["question5"])
    # Questions for Policy Area 2
    pol_energy1 = make_likert6(Lexicon.vignettes["PolicyArea2"]["question1"])
    pol_energy2 = make_likert6(Lexicon.vignettes["PolicyArea2"]["question2"])
    pol_energy3 = make_likert6(Lexicon.vignettes["PolicyArea2"]["question3"])
    pol_energy4 = make_likert6(Lexicon.vignettes["PolicyArea2"]["question4"])
    pol_energy5 = make_likert6(Lexicon.vignettes["PolicyArea2"]["question5"])
    # Questions for Policy Area 3
    pol_co2tax1 = make_likert6(Lexicon.vignettes["PolicyArea3"]["question1"])
    pol_co2tax2 = make_likert6(Lexicon.vignettes["PolicyArea3"]["question2"])
    pol_co2tax3 = make_likert6(Lexicon.vignettes["PolicyArea3"]["question3"])
    pol_co2tax4 = make_likert6(Lexicon.vignettes["PolicyArea3"]["question4"])
    pol_co2tax5 = make_likert6(Lexicon.vignettes["PolicyArea3"]["question5"])
    # Questions for Policy Area 4
    pol_bldins1 = make_likert6(Lexicon.vignettes["PolicyArea4"]["question1"])
    pol_bldins2 = make_likert6(Lexicon.vignettes["PolicyArea4"]["question2"])
    pol_bldins3 = make_likert6(Lexicon.vignettes["PolicyArea4"]["question3"])
    pol_bldins4 = make_likert6(Lexicon.vignettes["PolicyArea4"]["question4"])
    pol_bldins5 = make_likert6(Lexicon.vignettes["PolicyArea4"]["question5"])



# FUNCTIONS
def creating_session(subsession: Subsession):
    players = subsession.get_players()
    
    directions = ['left', 'right']
    
    # Generate all possible left/right combinations with at least one of each for the first two framings and the last two framings
    lr_combinations_1_2 = [p for p in itertools.product(directions, repeat=2)]
    lr_combinations_3_4 = [p for p in itertools.product(directions, repeat=2)]
    
    # create specific combinations for Framing 1 & 2 and Framing 3 & 4 tied to their policy areas
    combinations_1_2 = []
    combinations_3_4 = []
    
    for lr_1_2 in lr_combinations_1_2:
        combinations_1_2.append([('PolicyArea1', 'Framing1', lr_1_2[0]), ('PolicyArea2', 'Framing2', lr_1_2[1])])
        combinations_1_2.append([('PolicyArea1', 'Framing2', lr_1_2[0]), ('PolicyArea2', 'Framing1', lr_1_2[1])])
    
    for lr_3_4 in lr_combinations_3_4:
        combinations_3_4.append([('PolicyArea3', 'Framing3', lr_3_4[0]), ('PolicyArea4', 'Framing4', lr_3_4[1])])
        combinations_3_4.append([('PolicyArea3', 'Framing4', lr_3_4[0]), ('PolicyArea4', 'Framing3', lr_3_4[1])])
    
    # Combine and filter combinations to exclude all left or all right
    all_possible_combinations = [comb_1_2 + comb_3_4 for comb_1_2 in combinations_1_2 for comb_3_4 in combinations_3_4]
    filtered_combinations = [
        combo for combo in all_possible_combinations 
        if not (all(item[2] == 'left' for item in combo) or all(item[2] == 'right' for item in combo))
    ]

    # Shuffle to ensure randomness
    #random.shuffle(filtered_combinations)
    
    for i, player in enumerate(players):
        selection = filtered_combinations[i % len(filtered_combinations)]

        
        # Shuffle to randomize the order for each player
        randomized_selection = random.sample(selection, len(selection))
        
        # Assign the policy framing to participant vars
        player.participant.vars['policy_framing'] = randomized_selection
    


# PAGES
class BaseVignettePage(Page):
    @staticmethod
    def vars_for_template(player):
        policy_area, framing, direction = player.participant.vars['policy_framing'][player.round_number - 1]
        
        vignette = Lexicon.vignettes[policy_area][framing][direction]
        
        return {
            'headline': vignette['headline'],
            'content': vignette['content']
        }

class QuestionsPage(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        policy_area, framing, direction = player.participant.vars['policy_framing'][player.round_number - 1]

        
        question_field_map = {
            'PolicyArea1': ['pol_evehic1', 'pol_evehic2', 'pol_evehic3', 'pol_evehic4', 'pol_evehic5'],
            'PolicyArea2': ['pol_energy1', 'pol_energy2', 'pol_energy3', 'pol_energy4', 'pol_energy5'],
            'PolicyArea3': ['pol_bldins1', 'pol_bldins2', 'pol_bldins3', 'pol_bldins4', 'pol_bldins5'],
            'PolicyArea4': ['pol_co2tax1', 'pol_co2tax2', 'pol_co2tax3', 'pol_co2tax4', 'pol_co2tax5'],
        }
        
        return question_field_map[policy_area]

class VignettePage(BaseVignettePage):
    pass


class QuestionsPage(QuestionsPage):
    pass


page_sequence = [VignettePage, QuestionsPage]
