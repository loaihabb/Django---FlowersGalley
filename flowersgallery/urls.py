"""
URL configuration for flowersgallery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns #* (5) : if we need to use more than one language we must add this here
from django.conf import settings

urlpatterns = [
    path("il8n/", include("django.conf.urls.i18n")) #* (4) : if we need to use more than one language we must add this here
] 

urlpatterns += i18n_patterns ( #* (6) : if we need to use more than one language we must add this here
    path('admin/', admin.site.urls),
    path('', include("gallery.urls", namespace="gallery")),
    path('', include("interaction.urls", namespace="interaction")),
    path("accounts/", include("registration.urls", namespace="registration"))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#? In here all of the urls will be like ar/admin, we dont need the language to be ar/il8n too 
 