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
    NUM_ROUNDS = 5

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Questions for Policy Area 1
    pol_evehic1 = make_likert6(Lexicon.vignettes["pol_evehic"]["question1"])
    pol_evehic2 = make_likert6(Lexicon.vignettes["pol_evehic"]["question2"])
    pol_evehic3 = make_likert6(Lexicon.vignettes["pol_evehic"]["question3"])
    pol_evehic4 = make_likert6(Lexicon.vignettes["pol_evehic"]["question4"])
    pol_evehic5 = make_likert6(Lexicon.vignettes["pol_evehic"]["question5"])
    # Questions for Policy Area 2
    pol_energy1 = make_likert6(Lexicon.vignettes["pol_energy"]["question1"])
    pol_energy2 = make_likert6(Lexicon.vignettes["pol_energy"]["question2"])
    pol_energy3 = make_likert6(Lexicon.vignettes["pol_energy"]["question3"])
    pol_energy4 = make_likert6(Lexicon.vignettes["pol_energy"]["question4"])
    pol_energy5 = make_likert6(Lexicon.vignettes["pol_energy"]["question5"])
    # Questions for Policy Area 3
    pol_bldins1 = make_likert6(Lexicon.vignettes["pol_bldins"]["question1"])
    pol_bldins2 = make_likert6(Lexicon.vignettes["pol_bldins"]["question2"])
    pol_bldins3 = make_likert6(Lexicon.vignettes["pol_bldins"]["question3"])
    pol_bldins4 = make_likert6(Lexicon.vignettes["pol_bldins"]["question4"])
    pol_bldins5 = make_likert6(Lexicon.vignettes["pol_bldins"]["question5"])
    # Questions for Policy Area 4
    pol_co2tax1 = make_likert6(Lexicon.vignettes["pol_co2tax"]["question1"])
    pol_co2tax2 = make_likert6(Lexicon.vignettes["pol_co2tax"]["question2"])
    pol_co2tax3 = make_likert6(Lexicon.vignettes["pol_co2tax"]["question3"])
    pol_co2tax4 = make_likert6(Lexicon.vignettes["pol_co2tax"]["question4"])
    pol_co2tax5 = make_likert6(Lexicon.vignettes["pol_co2tax"]["question5"])

    # initializing variables to store info on displayed vignettes
    policy_area = models.StringField()
    framing = models.StringField()
    direction = models.StringField()

    #attention check
    AttCheck_Q1 = make_likert6(Lexicon.AttCheck_Q1)
    AttCheck_Q2 = make_likert6(Lexicon.AttCheck_Q2)
    AttCheck_Q3 = make_likert6(Lexicon.AttCheck_Q3)
    AttCheck_Q4 = make_likert6(Lexicon.AttCheck_Q4)
    AttCheck_Q5 = make_likert6(Lexicon.AttCheck_Q5)
    
    failed_attention_check = models.BooleanField(initial=False)

    #saving participant label to long format
    #to be tested when implemented online
    mfi_id = models.StringField()





# FUNCTIONS
def creating_session(subsession: Subsession):
    players = subsession.get_players()

    for player in players:
            player.mfi_id = player.participant.label

    framing_methods = ['TempFraming', 'RiskFraming', 'SociFraming', 'EconFraming']
    directions = ['left', 'right']

    policy_areas_1_2 = ['pol_evehic', 'pol_energy']
    policy_areas_3_4 = ['pol_bldins', 'pol_co2tax']

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

    random.shuffle(final_combinations_with_methods)
       
    for i, player in enumerate(players):
        combination = final_combinations_with_methods[i % len(final_combinations_with_methods)]
        
        random_policy_areas_1_2 = random.sample(policy_areas_1_2, len(policy_areas_1_2))
        random_policy_areas_3_4 = random.sample(policy_areas_3_4, len(policy_areas_3_4))
        
        updated_combination = []
        for fm, direction in combination:
            if 'TempFraming' in fm or 'RiskFraming' in fm:
                policy_area = random_policy_areas_1_2.pop(0)
            else:
                policy_area = random_policy_areas_3_4.pop(0)
            updated_combination.append((policy_area, fm, direction))

        randomized_selection = random.sample(updated_combination, len(updated_combination))
        player.participant.vars['policy_framing'] = randomized_selection

# PAGES
class BaseVignettePage(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player):
        if player.round_number == 2:  # Attention check round
            return {
                'headline': Lexicon.AttCheck_headline,
                'content': Lexicon.AttCheck_content,
                'round_number': player.round_number,
                'attention_check': True  # Flag to indicate an attention check
            }
        else:
            policy_area, framing, direction = player.participant.vars['policy_framing'][player.round_number - 1 if player.round_number < 2 else player.round_number - 2]
            player.policy_area = policy_area
            player.framing = framing
            player.direction = direction

            vignette = Lexicon.vignettes[policy_area][framing][direction]
            
            return {
                'headline': vignette['headline'],
                'content': vignette['content'],
                'round_number': player.round_number,
                'attention_check': False
            }

    @staticmethod
    def get_form_fields(player):
        if player.round_number == 2:
            return ['AttCheck_Q1', 'AttCheck_Q2', 'AttCheck_Q3', 'AttCheck_Q4', 'AttCheck_Q5']
        else:
            policy_area, _, _ = player.participant.vars['policy_framing'][player.round_number - 1 if player.round_number < 2 else player.round_number - 2]
            question_field_map = {
                'pol_evehic': ['pol_evehic1', 'pol_evehic2', 'pol_evehic3', 'pol_evehic4', 'pol_evehic5'],
                'pol_energy': ['pol_energy1', 'pol_energy2', 'pol_energy3', 'pol_energy4', 'pol_energy5'],
                'pol_bldins': ['pol_bldins1', 'pol_bldins2', 'pol_bldins3', 'pol_bldins4', 'pol_bldins5'],
                'pol_co2tax': ['pol_co2tax1', 'pol_co2tax2', 'pol_co2tax3', 'pol_co2tax4', 'pol_co2tax5'],
            }
            return question_field_map[policy_area]
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        # Check if it's the attention check round
        if player.round_number == 2:
            correct_answers = [1, 2, 3, 4, 5]
            actual_answers = [
                player.AttCheck_Q1, 
                player.AttCheck_Q2, 
                player.AttCheck_Q3, 
                player.AttCheck_Q4, 
                player.AttCheck_Q5
            ]
            
            # Determine if any of the answers do not match their expected values
            player.failed_attention_check = not all(actual == correct for actual, correct in zip(actual_answers, correct_answers))
        else:
            player.failed_attention_check = False

class AttentionCheckFailedPage(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 2 and player.failed_attention_check
    
    @staticmethod
    def vars_for_template(player: Player):
        return{
            'participantid': player.participant.label
        }

class VignettePage(BaseVignettePage):
    pass



page_sequence = [VignettePage, AttentionCheckFailedPage]
