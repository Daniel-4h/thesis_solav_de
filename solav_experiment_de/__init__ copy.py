import random

from otree.api import *

from settings import LANGUAGE_CODE

doc = """
How to translate an app to multiple languages (e.g. English and German).

There are 2 ways to define localizable strings:
(1) Put it in a "lexicon" file (see lexicon_en.py, lexicon_de.py).
    This is the easiest technique, and it allows you to easily reuse the same string multiple times.
(2) If the string contains variables, then it should to be defined in the template.
    Use an if-statement, like {{ if de }} Nein {{ else }} No {{ endif }}

When you change the LANGUAGE_CODE in settings.py, the language will automatically be changed.

Note: this technique does not require .po files, which are a more complex technique.    
"""

if LANGUAGE_CODE == 'de':
    from .lexicon_de import Lexicon
elif LANGUAGE_CODE == 'zh_hans':
    from .lexicon_zh_hans import Lexicon
else:
    from .lexicon_en import Lexicon


# this is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if de }} Nein {{ else }} No {{ endif }}
which_language = {'en': False, 'de': False, 'zh_hans': False}  # noqa
which_language[LANGUAGE_CODE[:2]] = True


class C(BaseConstants):
    NAME_IN_URL = 'panel_study'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# custom function to automatically make likert type fields with 5 options
# custom function to automatically make 4 option fields
def make_options4(label):
        return models.IntegerField(
            choices=[1,2,3,4],
            label=label,
            widget=widgets.RadioSelect,
            )

def make_no_yes(label):
        return models.IntegerField(
            choices=[0,1],
            label=label,
            widget=widgets.RadioSelect,
            )

def make_likert5(label):
        return models.IntegerField(
            choices=[1,2,3,4,5],
            label=label,
            widget=widgets.RadioSelect,
            )

def make_likert7(label):
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7],
            label=label,
            widget=widgets.RadioSelect,
            )

# 9-point likert scale with scaling for biospheric values
def make_likert9(label):
        return models.IntegerField(
            choices=[-1,0,1,2,3,4,5,6,7],
            label=label,
            widget=widgets.RadioSelect,
            )

def make_likert10(label):
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7,8,9,10],
            label=label,
            widget=widgets.RadioSelect,
            )

# functions to generate education and party choices based on language
def get_education_choices(language_code):
    education_choices = []

    if language_code == 'de':
        education_choices = [    
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
        ]
    elif language_code == 'zh_hans':
        education_choices = [
            # Add choices for Chinese language if needed
        ]
    else:
        education_choices = [
            Lexicon.high_school,
            Lexicon.some_college,
            Lexicon.bachelors_degree,
            Lexicon.masters_degree,
            Lexicon.doctoral_degree,
        ]
    return education_choices

def get_party_choices(language_code):
    party_choices = []
    if language_code == 'de':
        party_choices = [    
            Lexicon.cdcsu,
            Lexicon.spd,
            Lexicon.gruene,
            Lexicon.fdp,
            Lexicon.linke,
            Lexicon.afd,
            Lexicon.other_party
        ]
    elif language_code == 'zh_hans':
        party_choices = [
            # Add choices for Chinese language if needed
        ]
    else:
        party_choices = [
            Lexicon.republicans, 
            Lexicon.democrats, 
            Lexicon.independent_party, 
            Lexicon.other_party
        ]
    return party_choices

class Player(BasePlayer):
    ### Climate Change Concern Scale by Tobler et al. 2012
    ccc1 = make_likert5(Lexicon.ccc1Label) ## concern 4 items
    ccc2 = make_likert5(Lexicon.ccc2Label)
    ccc3 = make_likert5(Lexicon.ccc3Label)
    ccc4 = make_likert5(Lexicon.ccc4Label)
    ccc10 = make_likert5(Lexicon.ccc10Label) ## skepticism 7 items
    ccc11 = make_likert5(Lexicon.ccc11Label)
    ccc12 = make_likert5(Lexicon.ccc12Label)
    ccc13 = make_likert5(Lexicon.ccc13Label)
    ccc14 = make_likert5(Lexicon.ccc14Label)
    ccc15 = make_likert5(Lexicon.ccc15Label)
    ccc16 = make_likert5(Lexicon.ccc16Label)

    ### Climate Change Emotions Scale based on Knauf 2022 and Truelove 2012
    cce1 = make_likert5(Lexicon.cce1Label) ## Anger
    cce2 = make_likert5(Lexicon.cce2Label) ## Fear/Worry
    cce3 = make_likert5(Lexicon.cce3Label) ## Sadness
    cce4 = make_likert5(Lexicon.cce4Label) ## Joy
    cce5 = make_likert5(Lexicon.cce5Label) ## Curiosity
    cce6 = make_likert5(Lexicon.cce6Label) ## Hope

    ### Climate Change Knowledge by van der Linden 2015
    cck1  = make_options4(Lexicon.cck1Label)
    cck2  = make_options4(Lexicon.cck2Label)
    cck3  = make_options4(Lexicon.cck3Label)
    cck4  = make_options4(Lexicon.cck4Label)
    cck5  = make_options4(Lexicon.cck5Label)
    cck6  = make_options4(Lexicon.cck6Label)
    cck7  = make_options4(Lexicon.cck7Label)
    cck8  = make_options4(Lexicon.cck8Label)
    cck9  = make_options4(Lexicon.cck9Label)
    cck10 = make_options4(Lexicon.cck10Label)
    cck11 = make_options4(Lexicon.cck11Label)
    cck12 = make_options4(Lexicon.cck12Label)
    cck13 = make_options4(Lexicon.cck13Label)
   
    # (Dis)trust in climate science scale Sarathchandra & Haltinner, 2021
    cst1 = make_likert5(Lexicon.cst1Label)
    cst2 = make_likert5(Lexicon.cst2Label)
    cst3 = make_likert5(Lexicon.cst3Label)
    cst4 = make_likert5(Lexicon.cst4Label)
    cst5 = make_likert5(Lexicon.cst5Label)
    cst6 = make_likert5(Lexicon.cst6Label)

    # Personal efficacy Leiserowitz et al, 2010
    pe1 = make_likert7(Lexicon.pe1Label)
    pe2 = make_likert7(Lexicon.pe2Label)
    pe3 = make_likert7(Lexicon.pe3Label)

    # Worldviews and values - Hierarchy-Egalitarianism & Individualism-Communitarianism  
    wvv1 = make_likert7(Lexicon.wvv1Label)
    wvv2 = make_likert7(Lexicon.wvv2Label)
    wvv3 = make_likert7(Lexicon.wvv3Label)
    wvv4 = make_likert7(Lexicon.wvv4Label)
    wvv5 = make_likert7(Lexicon.wvv5Label)
    wvv6 = make_likert7(Lexicon.wvv6Label)

    # Importance of biospheric values van der Linden, 2015  
    ibv1 = make_likert9(Lexicon.ibv1Label)
    ibv2 = make_likert9(Lexicon.ibv2Label)
    ibv3 = make_likert9(Lexicon.ibv3Label)
    ibv4 = make_likert9(Lexicon.ibv4Label)

    # Political Orientation Pennycook et al 2020
    po1 = make_likert5(Lexicon.po1Label)
    po2 = make_likert5(Lexicon.po2Label)

    # Trust in political institutions from Eurobarometer / Lantian et al 2016  
    pit1 = make_likert7(Lexicon.pit1Label)
    pit2 = make_likert7(Lexicon.pit2Label)
    pit3 = make_likert7(Lexicon.pit3Label)
    pit4 = make_likert7(Lexicon.pit4Label)

  
  
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
        choices=get_education_choices(LANGUAGE_CODE),
    )

    residential_area = models.StringField(
        label=Lexicon.residential_area_label,
        choices=[Lexicon.metropolitan_area, Lexicon.suburban, Lexicon.rural],
    )

    zip_code = models.StringField(
        label=Lexicon.zip_code_label,
        blank=True,
    )

    party_affiliation = models.StringField(
        label=Lexicon.party_affiliation_label,
        choices=get_party_choices(LANGUAGE_CODE),
    )


class CCConcern(Page):
    form_model = 'player'
    form_fields= ['ccc1', 'ccc2', 'ccc3', 'ccc4',  'ccc10', 'ccc11', 'ccc12', 'ccc13', 'ccc14', 'ccc15', 'ccc16'  ]
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
class CCEmotion(Page):
    form_model = 'player'
    form_fields= ['cce1', 'cce2', 'cce3', 'cce4', 'cce5', 'cce6']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
    
class CCKnowledge(Page):
    form_model = 'player'
    form_fields= ['cck1', 'cck2', 'cck3', 'cck4',  'cck5', 'cck6', 'cck7', 'cck8', 'cck9', 'cck10', 'cck11', 'cck12', 'cck13']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
class CSTrust(Page):
    form_model = 'player'
    form_fields= ['cst1', 'cst2', 'cst3', 'cst4', 'cst5', 'cst6']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

class PEfficacy(Page):
    form_model = 'player'
    form_fields= ['pe1', 'pe2', 'pe3']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
class WVValues(Page):
    form_model = 'player'
    form_fields= ['wvv1', 'wvv2', 'wvv3', 'wvv4', 'wvv5', 'wvv6']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

class IBValues(Page):
    form_model = 'player'
    form_fields= ['ibv1', 'ibv2', 'ibv3', 'ibv4']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
class PolOrientation(Page):
    form_model = 'player'
    form_fields= ['po1', 'po2']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
class PITrust(Page):
    form_model = 'player'
    form_fields= ['pit1', 'pit2', 'pit3', 'pit4']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    


    
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'income', 'education', 'residential_area', 'zip_code', 'party_affiliation']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

# for easier visual adjustments, all scales with long anchors are moved to the beginning of the app. for the original order of scales, see copy below. 
page_sequence = [IBValues, CCConcern, WVValues, CCConcern, CCEmotion, CCKnowledge, CSTrust, PEfficacy, PolOrientation, PITrust, 
                 Demographics]
# copy pf page_sequence with original order of scales 
# page_sequence = [CCConcern, CCEmotion, GWNorms, CCKnowledge, CSTrust, PEfficacy, WVValues, IBValues, PolOrientation, PITrust, OVTrust, CRTask, EffCompletion, Demographics]