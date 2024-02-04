def make_likert7(label):
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7],
            label=label,
            widget=widgets.RadioSelect,
            )