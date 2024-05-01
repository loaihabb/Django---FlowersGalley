from django.views.generic import CreateView, UpdateView
from django.http import HttpResponseRedirect
from gallery.models import Flower
from .models import Action

class LikeFlowerView(CreateView, UpdateView):
    http_method_names = ["post"]
    model = Action
    fields = ("liked", )
    success_url = "/"
    success_url2 = "/en/flower/"

    def get_object(self, queryset=None):  #* If there's a user and trying to get the object, show the object, if not so create the object, from the database
        return Action.objects.get_or_create(
            user=self.request.user,
            flower_id=self.kwargs.get("flower_id")
        )[0] #* The second field is True or False so we don't need it 

    def _like_or_dislike(self): #* If the user did liked or not
        if self.request.POST.get("like"):
            return True
        elif self.request.POST.get("dislike"):
            return False
        return None

    def form_valid(self, form): #* Change the informations and show to the user
        interaction = self.get_object()
        interaction.liked = self._like_or_dislike()
        interaction.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        flower_id = self.kwargs.get("flower_id")
        return f"{self.success_url2}{flower_id}/"
