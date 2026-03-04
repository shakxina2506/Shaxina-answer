from django.urls import path
from .views import feedback_list
urlpatterns = [
    path('', feedback_list, name='feedback_list'),
]