from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)
import random


from .lexicon import Lexicon
def make_likert7(label):
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7],
            label=label,
            widget=widgets.RadioSelect,
            )

            
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
    # Questions for Policy Area 1
    q11 = make_likert7(Lexicon.vignettes["PolicyArea1"]["question1"])
    q12 = make_likert7(Lexicon.vignettes["PolicyArea1"]["question2"])
    q13 = make_likert7(Lexicon.vignettes["PolicyArea1"]["question3"])
    q14 = make_likert7(Lexicon.vignettes["PolicyArea1"]["question4"])
    q15 = make_likert7(Lexicon.vignettes["PolicyArea1"]["question5"])

    
    # Questions for Policy Area 2
    q21 = make_likert7(Lexicon.vignettes["PolicyArea2"]["question1"])
    q22 = make_likert7(Lexicon.vignettes["PolicyArea2"]["question2"])
    q23 = make_likert7(Lexicon.vignettes["PolicyArea2"]["question3"])
    q24 = make_likert7(Lexicon.vignettes["PolicyArea2"]["question4"])
    q25 = make_likert7(Lexicon.vignettes["PolicyArea2"]["question5"])

    
    # Questions for Policy Area 3
    q31 = make_likert7(Lexicon.vignettes["PolicyArea3"]["question1"])
    q32 = make_likert7(Lexicon.vignettes["PolicyArea3"]["question2"])
    q33 = make_likert7(Lexicon.vignettes["PolicyArea3"]["question3"])
    q34 = make_likert7(Lexicon.vignettes["PolicyArea3"]["question4"])
    q35 = make_likert7(Lexicon.vignettes["PolicyArea3"]["question5"])


    # Questions for Policy Area 4
    q41 = make_likert7(Lexicon.vignettes["PolicyArea4"]["question1"])
    q42 = make_likert7(Lexicon.vignettes["PolicyArea4"]["question2"])
    q43 = make_likert7(Lexicon.vignettes["PolicyArea4"]["question3"])
    q44 = make_likert7(Lexicon.vignettes["PolicyArea4"]["question4"])
    q45 = make_likert7(Lexicon.vignettes["PolicyArea4"]["question5"])
