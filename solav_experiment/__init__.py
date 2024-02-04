from otree.api import *
import random

author = 'Your Name'
doc = """
Your experiment description
"""

class Constants(BaseConstants):
    NAME_IN_URL = 'solav_experiment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 4  # Since there are four pages with vignettes

class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            # Randomize block order
            player.participant.vars['block_order'] = random.sample(['Block1', 'Block2'], 2)

            # Randomize framing order within each block
            player.participant.vars['framing_order'] = {
                'Block1': random.sample(['Framing1', 'Framing2'], 2),
                'Block2': random.sample(['Framing1', 'Framing2'], 2)
            }

            # Randomize policy areas
            player.participant.vars['policy_areas'] = {
                'Block1': random.choice(['PolicyArea1', 'PolicyArea2']),
                'Block2': 'PolicyArea2' if player.participant.vars['policy_areas']['Block1'] == 'PolicyArea1' else 'PolicyArea1'
            }

            # Randomize political positioning for each vignette
            player.participant.vars['political_positioning'] = [random.choice(['Left', 'Right']) for _ in range(4)]

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

# Define your page classes here if needed