from django import forms
from .models import Flower
#* from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
# class ContactUsForm(forms.Form):
#     name = forms.CharField()

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        #fields = "__all__"
        exclude = ["user", ] 
        labels = {
            "description" : ("The Description")
        }
        help_text = {
            "description" : ("Some useful help text")
        }
        widgets = {
            "description" : forms.Textarea(attrs={"cols": 40, "rows": 10})
        }

class FlowerUpdateForm(FlowerForm): #* This is inheritance 
    def clean_title(self):
        title = self.cleaned_data["title"]
        if "Flower" not in title.lower() and "flower" not in title.lower():
            raise ValidationError(("Your title doesn't contain the word flower"))
        return title
    # def clean(self):
    #     pass
        