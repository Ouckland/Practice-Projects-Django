from django.urls import path
from . import views
# from django.conf import Settings

app_name = 'music_engine'

urlpatterns = [
    path('', views.home, name='home'),
    path('display/artists/', views.display_artists, name="display_artists"),
    path('add/artist/', views.add_artist, name="add_artist"),
    path('delete-artist/<int:id>/', views.delete_artist, name="delete_artist"),
    path('update-artist/<int:id>/', views.update_artist, name="update_artist"),
]
