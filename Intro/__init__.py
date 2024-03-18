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

class Player(BasePlayer):
    dataScience = models.BooleanField(initial=False)
    dataTeach = models.BooleanField(initial=False)
    mobileDevice= models.BooleanField(initial=False, blank=True)

    include_participant = models.IntegerField(
        label = "Sind Sie älter als 18 Jahre und haben die deutsche Staatsbürgerschaft?",
        choices=[1,0],
        widget=widgets.RadioSelect,
    )

    exclusion = models.BooleanField(initial=False)

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

class Consent(Page):
    form_model = 'player'
    form_fields = ['dataScience', 'dataTeach', 'mobileDevice']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon)
    
class Instructions(Page):
    form_model = 'player'
    form_fields = []
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon)
    
class Introduction_SolAv(Page):
    form_model = 'player'
    form_fields = []
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon)

page_sequence = [InclusionQuestion, Exclusion, Consent, Instructions, Introduction_SolAv]
