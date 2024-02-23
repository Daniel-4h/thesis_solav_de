from otree.api import Page, WaitPage
from .models import Constants
from .lexicon import Lexicon
import random

class BaseVignettePage(Page):
    def vars_for_template(self):
        current_index = self.round_number - 1
        policy_area, framing = self.participant.vars['policy_framing_pairs'][current_index]

        # Randomly choose between 'alignleft' and 'alignright'
        alignment = random.choice(['alignleft', 'alignright'])
        vignette = Lexicon.vignettes[policy_area][framing][alignment]
        
        return {
            'headline': vignette['headline'],
            'content': vignette['content'],
        }

    def get_policy_area_and_framing(self):
        participant = self.participant
        round_number = self.round_number
        
        if round_number in [1, 3]:
            policy_area = participant.vars['policy_areas' if round_number == 1 else 'policy_areas_34'][0]
            framing = participant.vars['framings' if round_number == 1 else 'framings_34'][0]
        else:  # For rounds 2 and 4, swap policy areas and framings
            policy_area = participant.vars['policy_areas' if round_number == 2 else 'policy_areas_34'][1]
            framing = participant.vars['framings' if round_number == 2 else 'framings_34'][1]
        
        return policy_area, framing

class QuestionsPage(Page):
    form_model = 'player'
    
    def get_form_fields(self):
        current_index = self.round_number - 1
        policy_area, framing = self.participant.vars['policy_framing_pairs'][current_index]
        
        # Map policy areas to their question fields, assuming a naming convention
        question_field_map = {
            'PolicyArea1': ['q11', 'q12', 'q13', 'q14', 'q15'],
            'PolicyArea2': ['q21', 'q22', 'q23', 'q24', 'q25'],
            'PolicyArea3': ['q31', 'q32', 'q33', 'q34', 'q35'],
            'PolicyArea4': ['q41', 'q42', 'q43', 'q44', 'q45'],
        }
        
        return question_field_map[policy_area]


class VignettePage(BaseVignettePage):
    pass

class QuestionsPage(QuestionsPage):
    pass

page_sequence = [
    VignettePage, QuestionsPage
]