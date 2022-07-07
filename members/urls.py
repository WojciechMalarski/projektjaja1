from django.urls import path
from .views import UserRegisterView
urlpatterns = [
    # ex: /polls/
    path('register/', UserRegisterView.as_view(), name='register'),
    ]
