from otree.api import Page, WaitPage
from .models import Constants

class BaseVignettePage(Page):
    def vars_for_template(self):
        participant = self.participant
        block_order = participant.vars['block_order']
        framing_order = participant.vars['framing_order']
        policy_areas = participant.vars['policy_areas']
        political_positioning = participant.vars['political_positioning']
        
        current_block_index = (self.round_number - 1) // 2
        current_framing_index = (self.round_number - 1) % 2
        current_block = block_order[current_block_index]
        current_framing = framing_order[current_block][current_framing_index]
        current_policy_area = policy_areas[current_block]
        current_political_position = political_positioning[(self.round_number - 1)]

        return {
            'current_block': current_block,
            'current_framing': current_framing,
            'current_policy_area': current_policy_area,
            'current_political_position': current_political_position,
        }

# Vignette Pages
class VignettePage1(BaseVignettePage):
    pass

class VignettePage2(BaseVignettePage):
    pass

class VignettePage3(BaseVignettePage):
    pass

class VignettePage4(BaseVignettePage):
    pass

# Question Pages
class QuestionsForVignette1(Page):
    form_model = 'player'
    form_fields = ['question1', 'question2']  # Adapt these fields based on your model

class QuestionsForVignette2(Page):
    form_model = 'player'
    form_fields = ['question3', 'question4']  # Adapt these fields based on your model

class QuestionsForVignette3(Page):
    form_model = 'player'
    form_fields = ['question5', 'question6']  # Adapt these fields based on your model

class QuestionsForVignette4(Page):
    form_model = 'player'
    form_fields = ['question7', 'question8']  # Adapt these fields based on your model

page_sequence = [
    VignettePage1, QuestionsForVignette1,
    VignettePage2, QuestionsForVignette2,
    VignettePage3, QuestionsForVignette3,
    VignettePage4, QuestionsForVignette4
]