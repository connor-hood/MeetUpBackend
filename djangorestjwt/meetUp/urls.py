from .views import RegisterView, LoginView
from django.urls import path, include

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]