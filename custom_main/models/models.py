from django.db import models
from .base_models import BaseGeneralFieldModel
from hackcraft.models import Hackathons
# Create your models here.

class Widget(BaseGeneralFieldModel):
    key = models.CharField(max_length=17)
    type = models.CharField(max_length=50)
    hackathon = models.ForeignKey(Hackathons,on_delete=models.CASCADE)
    child = models.ForeignKey('self',on_delete=models.PROTECT,null=True)
    is_child = models.BooleanField()

    def __str__(self):
        return f'{self.key} - {self.hackathon.name}'

    def save(self, *args, **kwargs):
        if self.hackathon and self.hackathon.type == 'Custom':
            if self.child:
                self.is_child = True
            else:
                self.is_child = False
        else:
            raise ValueError('Hackathon type is not custom')
        super().save(*args, **kwargs)
