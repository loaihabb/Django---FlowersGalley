from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#* To create Manager to something (1)
class FLowerWithImageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(image = "") #* images is like home/leo/img

class Flower(models.Model):

    class Meta:
        permissions =[("test_flower", "Test Flower")]
        ordering = ["-title"]

    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    description_ar = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

#* (2)
    objects = models.Manager()
    with_images = FLowerWithImageManager()

    def __str__(self):
        return self.title # * Any Object in the database will take this, when deleting or showing etc...

