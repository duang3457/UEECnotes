
from django.urls import path
from forums.views import *

urlpatterns = [
    path('', forums, name= 'forums'),
]