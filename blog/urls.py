from django.urls import path
from .views import feedback_list,thanks
urlpatterns = [
    path('', feedback_list, name='feedback_list'),
    path('new/',thanks, name='thanks'),

]
