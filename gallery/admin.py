from django.contrib import admin
from .models import Flower
# * Register your models here.


class FlowerAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "image")


admin.site.register(Flower, FlowerAdmin)
