"""
URL configuration for art_generator project.

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
from django.urls import path, include
from art_app.views import profile, home, add_to_favorites, remove_from_favorites, add_comment, get_comments
from .views import generate_art
from django.contrib import admin

urlpatterns = [
    path('', home, name='home'),
    path('generate_art/', generate_art, name='generate_art'),
    path('profile/', profile, name='profile'),
    path('add_to_favorites/<int:art_id>/', add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:art_id>/', remove_from_favorites, name='remove_from_favorites'),
    path('add_comment/<int:art_id>/', add_comment, name='add_comment'),
    path('get_comments/<int:art_id>/', get_comments, name='get_comments'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('art_generator.urls')),
]
