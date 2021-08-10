from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('', RedirectView.as_view(url='/products'))
]