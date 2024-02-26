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

page_sequence = [Consent, Instructions, Introduction_SolAv]
