import random

from otree.api import *
from .lexicon import Lexicon

class C(BaseConstants):
    NAME_IN_URL = 'intro'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

def make_likert10(label):
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7,8,9,10],
            label=label,
            widget=widgets.RadioSelect,
            )

class Player(BasePlayer):
    mobileDevice= models.BooleanField(initial=False, blank=True)

    include_participant = models.IntegerField(
        label = "Sind Sie älter als 18 Jahre und besitzen die deutsche Staatsbürgerschaft?",
        choices=[1,0],
        widget=widgets.RadioSelect,
    )

    exclusion = models.BooleanField(initial=False)

    ### Pol Orientation
    po1 = make_likert10(Lexicon.po1Label)


### PAGES
class Consent(Page):
    form_model = 'player'
    form_fields = ['mobileDevice']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon)

class InclusionQuestion(Page):
    form_model = 'player'
    form_fields= ['include_participant']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon)
    
    def before_next_page(player, timeout_happened):
        if player.include_participant == 1:
            player.exclusion = False
        else:
            player.exclusion = True

class Exclusion(Page):
    @staticmethod
    def is_displayed(player):
        return player.exclusion
    
    @staticmethod
    def vars_for_template(player: Player):
        return{
            'participantid': player.participant.label
        }

class PolOrientation(Page):
    form_model = 'player'
    form_fields= ['po1']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon)
    
class Instructions(Page):
    form_model = 'player'
    form_fields = []
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon)

page_sequence = [Consent, InclusionQuestion, Exclusion, PolOrientation, Instructions]
