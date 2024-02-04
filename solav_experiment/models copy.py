import random
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)
from .lexicon import Lexicon

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

            # Correctly randomize framing order within each block
            player.participant.vars['framing_order'] = {
                'Block1': random.sample(['Framing1', 'Framing2'], 2),
                'Block2': random.sample(['Framing3', 'Framing4'], 2)  # Adjusted to use Framing3 and Framing4 for Block2
            }

            # Correctly randomize policy areas for Block 2 to include Policy Areas 3 & 4
            policy_area_for_block1 = random.choice(['PolicyArea1', 'PolicyArea2'])
            policy_area_for_block2 = random.choice(['PolicyArea3', 'PolicyArea4'])  # Updated choice to Policy Areas 3 & 4
            player.participant.vars['policy_areas'] = {
                'Block1': policy_area_for_block1,
                'Block2': policy_area_for_block2
            }

            # Randomize political positioning for each vignette
            player.participant.vars['political_positioning'] = [random.choice(['Left', 'Right']) for _ in range(4)]
            
class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Dynamically generate question fields based on the lexicon
    q1_block1_policyArea1 = make_likert7(Lexicon.vignettes['Block1']['PolicyArea1']['questions']['q1'])
    q2_block1_policyArea1 = make_likert7(Lexicon.vignettes['Block1']['PolicyArea1']['questions']['q2'])
    q3_block1_policyArea1 = make_likert7(Lexicon.vignettes['Block1']['PolicyArea1']['questions']['q3'])

    q1_block1_policyArea2 = make_likert7(Lexicon.vignettes['Block1']['PolicyArea2']['questions']['q1'])
    q2_block1_policyArea2 = make_likert7(Lexicon.vignettes['Block1']['PolicyArea2']['questions']['q2'])
    q3_block1_policyArea2 = make_likert7(Lexicon.vignettes['Block1']['PolicyArea2']['questions']['q3'])

    q1_block2_policyArea3 = make_likert7(Lexicon.vignettes['Block2']['PolicyArea3']['questions']['q1'])
    q2_block2_policyArea3 = make_likert7(Lexicon.vignettes['Block2']['PolicyArea3']['questions']['q2'])
    q3_block2_policyArea3 = make_likert7(Lexicon.vignettes['Block2']['PolicyArea3']['questions']['q3'])

    q1_block2_policyArea4 = make_likert7(Lexicon.vignettes['Block2']['PolicyArea4']['questions']['q1'])
    q2_block2_policyArea4 = make_likert7(Lexicon.vignettes['Block2']['PolicyArea4']['questions']['q2'])
    q3_block2_policyArea4 = make_likert7(Lexicon.vignettes['Block2']['PolicyArea4']['questions']['q3'])
