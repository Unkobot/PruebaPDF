from django.urls import path
from .views import HomeView

urlpatterns = [
    path('index/', HomeView.as_view(), name='home'),
]