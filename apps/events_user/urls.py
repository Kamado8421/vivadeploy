from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.global_events, name='global_events'),
]

handler404 = 'apps.auth_user.views.page_not_found'
