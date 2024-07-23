from django.contrib import admin
from hackcraft.models import Skill,UserProfile, Hackathons
from .models.models import Widget

# admin registeration of hackcraft models
admin.site.register(Skill)
admin.site.register(UserProfile)
admin.site.register(Hackathons)

admin.site.register(Widget)
