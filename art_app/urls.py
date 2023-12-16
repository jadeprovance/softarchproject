from django.urls import path
from .views import art_detail, add_to_favorites, remove_from_favorites, add_comment, get_comments, profile

urlpatterns = [
    path('art/<int:art_id>/', art_detail, name='art_detail'),
    path('add_to_favorites/<int:art_id>/', add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:art_id>/', remove_from_favorites, name='remove_from_favorites'),
    path('add_comment/<int:art_id>/', add_comment, name='add_comment'),
    path('get_comments/<int:art_id>/', get_comments, name='get_comments'),
    path('profile/', profile, name='profile'),
]
