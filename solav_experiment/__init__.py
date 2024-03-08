import random
from otree.api import *
from .lexicon import Lexicon


def make_likert7(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
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
    pol_evehic1 = make_likert7(Lexicon.vignettes["PolicyArea1"]["question1"])
    pol_evehic2 = make_likert7(Lexicon.vignettes["PolicyArea1"]["question2"])
    pol_evehic3 = make_likert7(Lexicon.vignettes["PolicyArea1"]["question3"])
    pol_evehic4 = make_likert7(Lexicon.vignettes["PolicyArea1"]["question4"])
    pol_evehic5 = make_likert7(Lexicon.vignettes["PolicyArea1"]["question5"])
    # Questions for Policy Area 2
    pol_energy1 = make_likert7(Lexicon.vignettes["PolicyArea2"]["question1"])
    pol_energy2 = make_likert7(Lexicon.vignettes["PolicyArea2"]["question2"])
    pol_energy3 = make_likert7(Lexicon.vignettes["PolicyArea2"]["question3"])
    pol_energy4 = make_likert7(Lexicon.vignettes["PolicyArea2"]["question4"])
    pol_energy5 = make_likert7(Lexicon.vignettes["PolicyArea2"]["question5"])
    # Questions for Policy Area 3
    pol_co2tax1 = make_likert7(Lexicon.vignettes["PolicyArea3"]["question1"])
    pol_co2tax2 = make_likert7(Lexicon.vignettes["PolicyArea3"]["question2"])
    pol_co2tax3 = make_likert7(Lexicon.vignettes["PolicyArea3"]["question3"])
    pol_co2tax4 = make_likert7(Lexicon.vignettes["PolicyArea3"]["question4"])
    pol_co2tax5 = make_likert7(Lexicon.vignettes["PolicyArea3"]["question5"])
    # Questions for Policy Area 4
    pol_bldins1 = make_likert7(Lexicon.vignettes["PolicyArea4"]["question1"])
    pol_bldins2 = make_likert7(Lexicon.vignettes["PolicyArea4"]["question2"])
    pol_bldins3 = make_likert7(Lexicon.vignettes["PolicyArea4"]["question3"])
    pol_bldins4 = make_likert7(Lexicon.vignettes["PolicyArea4"]["question4"])
    pol_bldins5 = make_likert7(Lexicon.vignettes["PolicyArea4"]["question5"])


# FUNCTIONS
def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        # Randomly decide the framing for Policy Areas 1 and 2, and similarly for 3 and 4
        framing_1_2 = random.sample(['Framing1', 'Framing2'], 2)
        framing_3_4 = random.sample(['Framing3', 'Framing4'], 2)
        # Pair policy areas with their framings
        policy_framing_pairs = [
            ('PolicyArea1', framing_1_2[0]),
            ('PolicyArea2', framing_1_2[1]),
            ('PolicyArea3', framing_3_4[0]),
            ('PolicyArea4', framing_3_4[1]),
        ]
        # Randomize the order of policy areas while keeping the framing rules
        random.shuffle(policy_framing_pairs)
        player.participant.vars['policy_framing_pairs'] = policy_framing_pairs


# PAGES
class BaseVignettePage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        current_index = player.round_number - 1
        policy_area, framing = player.participant.vars['policy_framing_pairs'][current_index]
        # Randomly choose between 'alignleft' and 'alignright'
        alignment = random.choice(['alignleft', 'alignright'])
        vignette = Lexicon.vignettes[policy_area][framing][alignment]
        return {
            'headline': vignette['headline'],
            'content': vignette['content'],
        }

class QuestionsPage(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        current_index = player.round_number - 1
        policy_area, framing = player.participant.vars['policy_framing_pairs'][current_index]
        # Map policy areas to their question fields, assuming a naming convention
        question_field_map = {
            'PolicyArea1': ['pol_evehic1', 'pol_evehic2', 'pol_evehic3', 'pol_evehic4', 'pol_evehic5'],
            'PolicyArea2': ['pol_energy1', 'pol_energy2', 'pol_energy3', 'pol_energy4', 'pol_energy5'],
            'PolicyArea3': ['pol_co2tax1', 'pol_co2tax2', 'pol_co2tax3', 'pol_co2tax4', 'pol_co2tax5'],
            'PolicyArea4': ['pol_bldins1', 'pol_bldins2', 'pol_bldins3', 'pol_bldins4', 'pol_bldins5'],
        }
        return question_field_map[policy_area]


class VignettePage(BaseVignettePage):
    pass


class QuestionsPage(QuestionsPage):
    pass


page_sequence = [VignettePage, QuestionsPage]
