from django.contrib import admin
from .models import Action
# Register your models here.

class ActionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Action, ActionAdmin)
