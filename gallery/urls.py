from django.urls import path, include
from .views import Home, FlowerDetailView, FlowerCreateView, FlowerUpdateView, FlowerDeleteView
app_name = "gallery"

urlpatterns = [
    path('', Home.as_view()),
    path('flower/<int:pk>/', FlowerDetailView.as_view(), name="flower-detail"),
    path('flower/create/', FlowerCreateView.as_view(), name="flower-create"),
    path('flower/<int:pk>/update/', FlowerUpdateView.as_view(), name="flower-update"),
    path('flower/<int:pk>/delete/', FlowerDeleteView.as_view(), name="flower-delete"),
]