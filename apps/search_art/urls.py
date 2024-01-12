from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', views.search_user, name='search_user'),
]

handler404 = 'apps.auth_user.views.page_not_found'
