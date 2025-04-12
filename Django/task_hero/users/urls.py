from django.urls import path
from django.contrib.auth import views as user_views

from . import views

app_name = 'users'

urlpatterns = [
    path('sign-up', views.sign_up(), name='sign_up'),
    path('log-in', user_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('log-out', user_views.LogoutView.as_view(), name='logout'),
]