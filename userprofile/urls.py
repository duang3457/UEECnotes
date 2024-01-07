from django.urls import path,include
from userprofile.views import *

urlpatterns = [
   path('', userprofile, name='userprofile'),
]