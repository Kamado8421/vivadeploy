from django.urls import path, include
from . import views

urlpatterns = [
    path('direct/', views.chats, name='chats'),
    path('groups/', views.groups, name='groups'),
]

handler404 = 'apps.auth_user.views.page_not_found'
