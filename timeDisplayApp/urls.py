from django.urls import path
from . import views
urlpatterns =[
    path('', views.red_to_timeDisplay),
    path('timeDisplay', views.index)
]