
from django.urls import path
from forums.views import *
from .views import PostList

urlpatterns = [
    path('forums/', forums, name='forums'),
    path('', welcome, name='welcome'),
    path('contact/', contact, name='contact'),
    path('ab/', ab, name="ab"),
    path('updatelog/', update_log, name='update_log'),
    path('api/posts/', PostList.as_view()),
]