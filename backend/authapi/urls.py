from django.urls import path
from .views import UserCreate
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('auth/register', UserCreate.as_view(), name='register'),
    path('auth/login', obtain_auth_token, name='login'),
    ]