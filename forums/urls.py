
from django.urls import path
from forums.views import *

urlpatterns = [
    path('forums/', forums, name='forums'),
    path('', welcome, name='welcome'),
    path('contact/', contact, name='contact'),
    path('ab/', ab, name="ab"),
    path('game1/', game_snake, name='snake'),
]