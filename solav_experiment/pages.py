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
    form_fields = ['q1_block1_policyArea1', 'q2_block1_policyArea1', 'q3_block1_policyArea1']
    template_name = 'solav_experiment/QuestionsVig1.html'

class QuestionsForVignette2(Page):
    form_model = 'player'
    form_fields = ['q1_block1_policyArea2', 'q2_block1_policyArea2', 'q3_block1_policyArea2']
    template_name = 'solav_experiment/QuestionsVig2.html'

class QuestionsForVignette3(Page):
    form_model = 'player'
    form_fields = ['q1_block2_policyArea3', 'q2_block2_policyArea3', 'q3_block2_policyArea3']
    template_name = 'solav_experiment/QuestionsVig3.html'

class QuestionsForVignette4(Page):
    form_model = 'player'
    form_fields = ['q1_block2_policyArea4', 'q2_block2_policyArea4', 'q3_block2_policyArea4']
    template_name = 'solav_experiment/QuestionsVig4.html'


page_sequence = [
    VignettePage1, QuestionsForVignette1,
    VignettePage2, QuestionsForVignette2,
    VignettePage3, QuestionsForVignette3,
    VignettePage4, QuestionsForVignette4
]