import random
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

def make_likert7(label):
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7],
            label=label,
            widget=widgets.RadioSelect,
            )

class Constants(BaseConstants):
    name_in_url = 'solav_experiment'
    num_rounds = 1
    players_per_group = None

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
            policy_area_for_block1 = random.choice(['PolicyArea1', 'PolicyArea2'])
            policy_area_for_block2 = 'PolicyArea2' if policy_area_for_block1 == 'PolicyArea1' else 'PolicyArea1'
            player.participant.vars['policy_areas'] = {
                'Block1': policy_area_for_block1,
                'Block2': policy_area_for_block2
            }

            # Randomize political positioning for each vignette
            player.participant.vars['political_positioning'] = [random.choice(['Left', 'Right']) for _ in range(4)]

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    ### Pol Orientation
    question1 = make_likert7("To what extent do you agree with the policy presented?")
    question2 = make_likert7("How effective do you believe this policy would be in practice?")
    question3 = make_likert7("How likely are you to support this policy?")
    question4 = make_likert7("To what extent do you agree with the policy presented?")
    question5 = make_likert7("How effective do you believe this policy would be in practice?")
    question6 = make_likert7("How likely are you to support this policy?")
    question7 = make_likert7("To what extent do you agree with the policy presented?")
    question8 = make_likert7("How effective do you believe this policy would be in practice?")
    question9 = make_likert7("How likely are you to support this policy?")
    # Add more questions as needed