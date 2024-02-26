from otree.api import *
import random

from .lexicon import Lexicon


class C(BaseConstants):
    NAME_IN_URL = 'personalinfo'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def make_likert11(label):
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7,8,9,10,11],
            label=label,
            widget=widgets.RadioSelect,
            )

class Player(BasePlayer):

    ### Pol Orientation
    po1 = make_likert11(Lexicon.po1Label)


    ### Demographics
    age = models.IntegerField(
        label=Lexicon.age_label,
        min=18,
    )

    gender = models.StringField(
    label=Lexicon.gender_label,
    choices=[Lexicon.female, Lexicon.male, Lexicon.diverse, Lexicon.other],
    )

    income = models.StringField(
        label=Lexicon.income_label,
        choices=[
            Lexicon.income_less_than_A,
            Lexicon.income_A_to_B,
            Lexicon.income_B_to_C,
            Lexicon.income_C_to_D,
            Lexicon.income_more_than_D,
            Lexicon.prefer_not_to_say,
        ],
    )

    education = models.StringField(
        label=Lexicon.education_label,
        choices=[    
            Lexicon.no_formal_education,
            Lexicon.elementary_school,
            Lexicon.secondary_school,
            Lexicon.higher_secondary_school,
            Lexicon.vocational_training,
            Lexicon.high_school,
            Lexicon.college_degree,
            Lexicon.master_degree,
            Lexicon.doctoral_degree,
            Lexicon.prefer_not_to_say_education
        ],
    )

    residential_area = models.StringField(
        label=Lexicon.residential_area_label,
        choices=[Lexicon.metropolitan_area, Lexicon.suburban, Lexicon.rural],
    )


    region = models.StringField(
        label="Aus welchem Bundesland kommen Sie?",
        choices=[    
            "Baden-Württemberg",
            "Bayern",
            "Berlin",
            "Brandenburg",
            "Bremen",
            "Hamburg",
            "Hessen",
            "Mecklenburg-Vorpommern",
            "Niedersachsen",
            "Nordrhein-Westfalen",
            "Rheinland-Pfalz",
            "Saarland",
            "Sachsen-Anhalt",
            "Sachsen",
            "Schleswig-Holstein",
            "Thüringen" 
        ],
    )

    party_affiliation = models.StringField(
        label=Lexicon.party_affiliation_label,
        choices=[    
            Lexicon.cdcsu,
            Lexicon.spd,
            Lexicon.gruene,
            Lexicon.fdp,
            Lexicon.linke,
            Lexicon.afd,
            Lexicon.bsw,
            Lexicon.fw,
            Lexicon.wu,
            Lexicon.other_party
        ],
    )

    use_data = models.IntegerField(
        label = "Können wir Ihre Antworten für unsere Studie berücksichtigen?",
        choices=[1,0],
        widget=widgets.RadioSelect
    )

# FUNCTIONS
# PAGES
class PolOrientation(Page):
    form_model = 'player'
    form_fields= ['po1']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon)

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'income', 'education', 'residential_area', 'region', 'party_affiliation']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon)
    
class Honesty(Page):
    form_model = 'player'
    form_fields = ['use_data']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon)


page_sequence = [PolOrientation, Demographics, Honesty]
