from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('galery_virtual', views.galery_virtual, name='galery_virtual'),
    path('events/', include('apps.events_user.urls'), name='events'),
    path('search/', include('apps.search_art.urls')),
]

handler404 = 'apps.auth_user.views.page_not_found'
