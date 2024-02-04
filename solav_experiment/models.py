from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)
import random

class Constants(BaseConstants):
    name_in_url = 'solav_experiment'
    players_per_group = None
    num_rounds = 4

class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
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

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    q11 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)
    q12 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)
    q13 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)
    q21 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)
    q22 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)
    q23 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)
    q31 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)
    q32 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)
    q33 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)
    q41 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)
    q42 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)
    q43 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)