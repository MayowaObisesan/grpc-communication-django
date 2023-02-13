import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Currency(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    user_id = models.IntegerField(default=0, null=False, blank=False)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
