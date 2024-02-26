import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'outro'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    pass
   

class Outro(Page):
    form_model = 'player'
    form_fields = []
  

page_sequence = [Outro]
