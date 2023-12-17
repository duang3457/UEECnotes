
from django.urls import path
from game.views import *

urlpatterns = [
    path('game/', game, name='game'),


]