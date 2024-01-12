from django.urls import path, include

from .views import self_profile, feed

urlpatterns = [
    path('', self_profile, name="my_profile"),
    path('feed/', feed, name='feed')
]

