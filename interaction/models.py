from django.db import models
from django.contrib.auth.models import User
from gallery.models import Flower
# Create your models here.

class Action(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE) #? If the user has deleted, delete everything in this table
    flower = models.ForeignKey(to=Flower, on_delete=models.CASCADE, related_name="actions")
    liked = models.BooleanField(null=True)

    class Meta:
        unique_together = ["user", "flower"]