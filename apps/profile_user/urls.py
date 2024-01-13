from django.urls import path, include

from .views import self_profile, feed, new_post

urlpatterns = [
    path('', self_profile, name="my_profile"),
    path('feed/', feed, name='feed'),
    path('new_post/', new_post, name='new_post'),
]

