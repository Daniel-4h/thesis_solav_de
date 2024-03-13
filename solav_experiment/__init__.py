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
    pol_bldins1 = make_likert6(Lexicon.vignettes["PolicyArea4"]["question1"])
    pol_bldins2 = make_likert6(Lexicon.vignettes["PolicyArea4"]["question2"])
    pol_bldins3 = make_likert6(Lexicon.vignettes["PolicyArea4"]["question3"])
    pol_bldins4 = make_likert6(Lexicon.vignettes["PolicyArea4"]["question4"])
    pol_bldins5 = make_likert6(Lexicon.vignettes["PolicyArea4"]["question5"])
    # Questions for Policy Area 4
    pol_co2tax1 = make_likert6(Lexicon.vignettes["PolicyArea3"]["question1"])
    pol_co2tax2 = make_likert6(Lexicon.vignettes["PolicyArea3"]["question2"])
    pol_co2tax3 = make_likert6(Lexicon.vignettes["PolicyArea3"]["question3"])
    pol_co2tax4 = make_likert6(Lexicon.vignettes["PolicyArea3"]["question4"])
    pol_co2tax5 = make_likert6(Lexicon.vignettes["PolicyArea3"]["question5"])

    # initializing variables to store info on displayed vignettes
    policy_area = models.StringField()
    framing = models.StringField()
    direction = models.StringField()



# FUNCTIONS
def creating_session(subsession: Subsession):
    players = subsession.get_players()
    
    framing_methods = ['Framing1', 'Framing2', 'Framing3', 'Framing4']
    directions = ['left', 'right']
    all_combinations = list(itertools.product(directions, repeat=4))
    
    combinations_by_right_count = {i: [] for i in range(5)}
    for combo in all_combinations:
        right_count = combo.count('right')
        combinations_by_right_count[right_count].append(combo)
    
    final_combinations = []
    for right_count, combos in combinations_by_right_count.items():
        repeats = 12 // len(combos)
        for combo in combos:
            final_combinations.extend([combo] * repeats)
    
    final_combinations_with_methods = [
        [(framing_methods[i], direction) for i, direction in enumerate(combo)]
        for combo in final_combinations
    ]
    
    policy_areas_1_2 = ['PolicyArea1', 'PolicyArea2']
    policy_areas_3_4 = ['PolicyArea3', 'PolicyArea4']
    
    for i, player in enumerate(players):
        combination = final_combinations_with_methods[i % len(final_combinations_with_methods)]
        
        random_policy_areas_1_2 = random.sample(policy_areas_1_2, len(policy_areas_1_2))
        random_policy_areas_3_4 = random.sample(policy_areas_3_4, len(policy_areas_3_4))
        
        updated_combination = []
        for fm, direction in combination:
            if 'Framing1' in fm or 'Framing2' in fm:
                policy_area = random_policy_areas_1_2.pop(0)
            else:
                policy_area = random_policy_areas_3_4.pop(0)
            updated_combination.append((policy_area, fm, direction))

        randomized_selection = random.sample(updated_combination, len(updated_combination))
        player.participant.vars['policy_framing'] = randomized_selection

# PAGES
class BaseVignettePage(Page):
    @staticmethod
    def vars_for_template(player):
        policy_area, framing, direction = player.participant.vars['policy_framing'][player.round_number - 1]
        
        player.policy_area = policy_area
        player.framing = framing
        player.direction = direction

        vignette = Lexicon.vignettes[policy_area][framing][direction]
        
        return {
            'headline': vignette['headline'],
            'content': vignette['content'],
            'round_number': player.round_number
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
