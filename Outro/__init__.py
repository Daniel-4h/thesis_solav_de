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
    #saving participant label to long format
    participantid_full = models.StringField()
   

class Outro(Page):
    form_model = 'player'
    form_fields = []

    @staticmethod
    def vars_for_template(player: Player):
        player.participantid_full = player.participant.label
        return{
            'participantid': player.participant.label
        }
  

page_sequence = [Outro]
