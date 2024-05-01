from django.forms import BaseModelForm
from django.shortcuts import render, HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .forms import FlowerForm, FlowerUpdateForm
from .models import Flower
from django.urls import reverse_lazy

#* Cannot enter any page without login 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.

def home(request):
    return render(request, "index.html")

'''
# * This is if we use View from generic but this is hard
# TODO : We need to use TemplateView here

class Home(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("This is view")

class Home(TemplateView):
    template_name = "index.html"
    def get_context_data(self, *args, **kwargs): # * This is if we need to use some variables in the html using jinja
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "counter" : 11
        })
    return context
    
'''
class Home(ListView):
    template_name = "home.html"
    model = Flower
    context_object_name = "flowers"
    paginate_by = 3

    #* For all objects
    queryset = Flower.objects.all()

    #? For just objects with images
    #* queryset = Flower.with_images.all()

class FlowerDetailView(DetailView):
    template_name = "detail.html"
    model = Flower
    context_object_name = "flower"

# class FlowerCreateView(FormView):
#     template_name = "create-flower.html"
#     form_class = FlowerForm
#     success_url = "/"

#     def form_valid(self, form):
#         print(form)
#         print("form was submitted....")
#         return super().form_valid(form)
        
    # def form_invalid(self, form):
    #     pass
    

class FlowerCreateView(LoginRequiredMixin ,PermissionRequiredMixin ,CreateView):
    model = Flower
    template_name = "create-flower.html"
    form_class = FlowerForm
    success_url = "/"

    #* For LoginRequiredMixin we need to add this too
    login_url = "/accounts/login/"

    #* Just the accounts who has the add flower permession can add a flower 
    permission_required = "gallery.add_flower"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class FlowerUpdateView(LoginRequiredMixin, UpdateView):
    model = Flower
    template_name = "update-flower.html"
    form_class = FlowerUpdateForm
    success_url = "/"
    # success_url = reverse_lazy('flower-detail')
    #* For LoginRequiredMixin we need to add this too
    login_url = "/accounts/login/"

    def form_valid(self, form):
        self.object = form.save(commit=False) #* To catch the object before it goes to the database
        self.object.user = self.request.user #* To get the user whom have the athentication
        self.object.save()
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs): #* If we need to add smt to the template, not in the models or anywhere
        kwargs.update({
            "user": self.object.user
        })
        return super().get_context_data(*args, **kwargs)
        


class FlowerDeleteView(LoginRequiredMixin, DeleteView):
    model = Flower
    template_name = "delete-flower.html"
    success_url = "/"
    
    #* For LoginRequiredMixin we need to add this too
    login_url = "/accounts/login/"

    