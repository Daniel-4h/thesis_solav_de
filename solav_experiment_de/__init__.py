from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def make_likert5(label):
        return models.IntegerField(
            choices=[1,2,3,4,5],
            label=label,
            widget=widgets.RadioSelect,
            )

def make_likert10(label):
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7,8,9,10],
            label=label,
            widget=widgets.RadioSelect,
            )

class Player(BasePlayer):
    ### Climate Change Concern Scale by Tobler et al. 2012
    ccc1 = make_likert5("Wir müssen das empfindliche Klimagleichgewicht schützen.") ## concern 4 items
    ccc2 = make_likert5("Der Klimaschutz ist wichtig für unsere Zukunft.")
    ccc3 = make_likert5("Ich mache mir Sorgen über den Zustand des Klimas.")
    ccc4 = make_likert5("Der Klimawandel hat ernste Folgen für die Menschheit und die Natur.")
    ccc10 = make_likert5("Der Klimawandel und seine Folgen werden in den Medien übertrieben.") ## skepticism 7 items
    ccc11 = make_likert5("Der Klimawandel ist ein betrügerisches Geschäft.")
    ccc12 = make_likert5("Solange Metereologen nicht einmal richtig das Wetter vorhersagen können, kann das Klima auch nicht zuverlässig vorhergesagt werden.")
    ccc13 = make_likert5("Es gibt wichtigere Probleme als den Klimaschutz.")
    ccc14 = make_likert5("Ich fühle mich nicht von dem Klimawandel bedroht.")
    ccc15 = make_likert5("Die Folgen des Klimawandels sind unvorhersehbar, deswegen ist mein klimafreundliches Verhalten vergeblich.")
    ccc16 = make_likert5("Klimaschutz behindert unnötigerweise das Wirtschaftswachstum.")

    ### Demographics
    age = models.IntegerField(
        label=Lexicon.age_label,
        min=18,
    )

    gender = models.StringField(
    label=Lexicon.gender_label,
    choices=[Lexicon.female, Lexicon.male, Lexicon.diverse, Lexicon.other],
    )

    income = models.StringField(
        label=Lexicon.income_label,
        choices=[
            Lexicon.income_less_than_A,
            Lexicon.income_A_to_B,
            Lexicon.income_B_to_C,
            Lexicon.income_C_to_D,
            Lexicon.income_more_than_D,
            Lexicon.prefer_not_to_say,
        ],
    )

    education = models.StringField(
        label=Lexicon.education_label,
        choices=get_education_choices(LANGUAGE_CODE),
    )

    residential_area = models.StringField(
        label=Lexicon.residential_area_label,
        choices=[Lexicon.metropolitan_area, Lexicon.suburban, Lexicon.rural],
    )

    zip_code = models.StringField(
        label=Lexicon.zip_code_label,
        blank=True,
    )

    party_affiliation = models.StringField(
        label=Lexicon.party_affiliation_label,
        choices=get_party_choices(LANGUAGE_CODE),
    )

    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    crt_bat = models.IntegerField(
        label='''
        A bat and a ball cost 22 dollars in total.
        The bat costs 20 dollars more than the ball.
        How many dollars does the ball cost?'''
    )
    crt_widget = models.IntegerField(
        label='''
        If it takes 5 machines 5 minutes to make 5 widgets,
        how many minutes would it take 100 machines to make 100 widgets?
        '''
    )
    crt_lake = models.IntegerField(
        label='''
        In a lake, there is a patch of lily pads.
        Every day, the patch doubles in size.
        If it takes 48 days for the patch to cover the entire lake,
        how many days would it take for the patch to cover half of the lake?
        '''
    )


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake']


page_sequence = [Demographics, CognitiveReflectionTest]
