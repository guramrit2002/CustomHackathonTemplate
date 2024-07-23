from django.db import models
import uuid

class BaseGeneralFieldModel(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
