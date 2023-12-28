from django.urls import path,include


urlpatterns = [
    path('profile/', include(('userprofile.urls', 'userprofile'), namespace="userprofile")),
]