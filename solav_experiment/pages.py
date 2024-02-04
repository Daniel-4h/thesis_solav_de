from otree.api import Page, WaitPage
from .models import Constants

class BaseVignettePage(Page):
    def is_displayed(self):
        return True
    
    def vars_for_template(self):
        # Retrieve participant vars
        participant = self.participant
        block_order = participant.vars['block_order']
        framing_order = participant.vars['framing_order']
        policy_areas = participant.vars['policy_areas']
        political_positioning = participant.vars['political_positioning']
        
        # Determine the current block, framing, and policy area
        current_block = block_order[(self.round_number - 1) // 2]  # 2 vignettes per block
        current_framing = framing_order[current_block][self.round_number % 2 - 1]
        current_policy_area = policy_areas[current_block]
        current_political_position = political_positioning[self.round_number - 1]

        return {
            'current_block': current_block,
            'current_framing': current_framing,
            'current_policy_area': current_policy_area,
            'current_political_position': current_political_position
        }


class VignettePage1(BaseVignettePage):
    pass


class VignettePage2(BaseVignettePage):
    pass


class VignettePage3(BaseVignettePage):
    pass


class VignettePage4(BaseVignettePage):
    pass


page_sequence = [VignettePage1, VignettePage2, VignettePage3, VignettePage4]