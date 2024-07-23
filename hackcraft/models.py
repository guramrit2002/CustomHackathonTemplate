from django.db import models
from custom_main.models.base_models import BaseGeneralFieldModel
import uuid
# Create your models here.

USER_TYPE = (
    ('student','student'),
    ('professional','professional')
)

HACKATHON_TYPE = (
    ('Custom','Custom'),
    ('Default','Default')
)


class Skill(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    skill_name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return str(self._id)
class UserProfile(BaseGeneralFieldModel):
    user_type = models.CharField(max_length=500, choices=USER_TYPE, default=' ', null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=250, default=' ')
    gender = models.CharField(max_length=250, default=' ')
    city = models.CharField(max_length=250, default=' ')
    organisation = models.CharField(max_length=250, default=' ')
    cousrse_name = models.CharField(max_length=250, default=' ')
    course_end_year = models.IntegerField(default=-1)
    date_of_birth = models.DateField(null=True)
    interest = models.JSONField(default={})
    about = models.CharField(max_length=3000, default=' ')
    education_qualification = models.CharField(max_length=100, default=' ')
    specialization = models.CharField(max_length=200, default=' ')
    percentage = models.IntegerField(default=-1)
    skill = models.ManyToManyField(Skill, default=None, blank=True)
    degree = models.CharField(max_length=200, default=' ')
    # social links
    facebook = models.CharField(max_length=100, default=' ')
    x = models.CharField(max_length=50, default=' ')
    instagram = models.CharField(max_length=100, default=' ')
    linkedin = models.CharField(max_length=100, default=' ')
    github = models.CharField(max_length=100, default=' ')
    medium = models.CharField(max_length=100, default=' ')
    reddit = models.CharField(max_length=100, default=' ')
    slack = models.CharField(max_length=100, default=' ')
    dribble = models.CharField(max_length=100, default=' ')
    behance = models.CharField(max_length=100, default=' ')
    codepen = models.CharField(max_length=100, default=' ')
    figma = models.CharField(max_length=100, default=' ')
    phone = models.CharField(max_length=10, null=True, default=' ')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} profile'

class Hackathons(BaseGeneralFieldModel):

    created_by = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='hackathon_user')
    type = models.CharField(
        max_length=50,
        choices=HACKATHON_TYPE
    )
    logo = models.CharField(
        max_length=2000,
        default="",
        blank=True)
    name = models.CharField(max_length=250)
    organisation_name = models.CharField(
        max_length=250,
        default=None)
    brief = models.TextField(default=None)
    deadline = models.DateField(
        auto_now=False,
        auto_now_add=False)
    start_date_time = models.DateTimeField(
        auto_now=False,
        auto_now_add=False)
    team_size_min = models.IntegerField()
    team_size_max = models.IntegerField(blank=True, null=True)
    fee = models.CharField(
        max_length=100,
        default=None,
        blank=True)
    total_number_rounds = models.IntegerField(
        blank=True,
        null=True)
    form_exist = models.BooleanField(default=False)
    number_of_registeration = models.IntegerField(
        blank=True,
        default=None,
        null=True)
    template = models.CharField(max_length=10, default=" ")

    def __str__(self) -> str:
        return self.name