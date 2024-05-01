from django.urls import path, include
from .views import LikeFlowerView

app_name = "interaction"

urlpatterns = [
    path('flower/<int:flower_id>/action/', LikeFlowerView.as_view(), name="like-flower"),
]