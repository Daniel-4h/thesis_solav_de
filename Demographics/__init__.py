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



class Player(BasePlayer):


    ### Demographics
    age = models.IntegerField(
        label=Lexicon.age_label,
        min=18,
    )

    gender = models.StringField(
        label=Lexicon.gender_label,
        choices=[
            ["f", Lexicon.female], 
            ["m", Lexicon.male], 
            ["d", Lexicon.diverse], 
            ["o", Lexicon.other]
        ],
        widget=widgets.RadioSelect,
    )

    income = models.IntegerField(
        label=Lexicon.income_label,
        choices=[
            [1, Lexicon.income_less_than_A],
            [2, Lexicon.income_A_to_B],
            [3, Lexicon.income_B_to_C],
            [4, Lexicon.income_C_to_D],
            [5, Lexicon.income_more_than_D],
            [6, Lexicon.prefer_not_to_say]
        ],
        widget=widgets.RadioSelect,
    )

    education = models.StringField(
        label=Lexicon.education_label,
        choices=[    
            ["noed", Lexicon.no_formal_education],
            ["eles", Lexicon.elementary_school],
            ["secs", Lexicon.secondary_school],
            ["hsec", Lexicon.higher_secondary_school],
            ["voct", Lexicon.vocational_training],
            ["hisc", Lexicon.high_school],
            ["coll", Lexicon.college_degree],
            ["ma", Lexicon.master_degree],
            ["phd", Lexicon.doctoral_degree],
            ["na", Lexicon.prefer_not_to_say_education]
        ],
        widget=widgets.RadioSelect,
    )

    residential_area = models.StringField(
        label=Lexicon.residential_area_label,
        choices=[
            ["metro", Lexicon.metropolitan_area],
            ["suburb", Lexicon.suburban], 
            ["rural", Lexicon.rural]
        ],
        widget=widgets.RadioSelect,
    )


    region = models.StringField(
        label="Aus welchem Bundesland kommen Sie?",
        choices=[
            ["bw", Lexicon.bw],
            ["by", Lexicon.by],
            ["be", Lexicon.be],
            ["br", Lexicon.br],
            ["hb", Lexicon.hb],
            ["hh", Lexicon.hh],
            ["he", Lexicon.he],
            ["mp", Lexicon.mp],
            ["ns", Lexicon.ns],
            ["nw", Lexicon.nw],
            ["rp", Lexicon.rp],
            ["sl", Lexicon.sl],
            ["sa", Lexicon.sa],
            ["sx", Lexicon.sx],
            ["sh", Lexicon.sh],
            ["th", Lexicon.th]
        ],
        widget=widgets.RadioSelect,
    )

    party_affiliation = models.StringField(
        label=Lexicon.party_affiliation_label,
        choices=[    
            ["cdu", Lexicon.cdcsu],
            ["spd", Lexicon.spd],
            ["gru", Lexicon.gruene],
            ["fdp", Lexicon.fdp],
            ["lin", Lexicon.linke],
            ["afd", Lexicon.afd],
            ["bsw", Lexicon.bsw],
            ["frw", Lexicon.fw],
            ["weu", Lexicon.wu],
            ["na", Lexicon.other_party]
        ],
        widget=widgets.RadioSelect,
    )

    use_data = models.IntegerField(
        label = "Können wir Ihre Antworten für unsere Studie berücksichtigen?",
        choices=[1,0],
        widget=widgets.RadioSelect,
    )

# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'age', 'gender', 'income', 'education', 'residential_area', 'region', 'party_affiliation']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon)
    
class Honesty(Page):
    form_model = 'player'
    form_fields = ['use_data']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon)


page_sequence = [Demographics
                 #, Honesty
                 ]
