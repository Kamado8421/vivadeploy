from django.contrib import admin
from django.urls import path, include

from apps.auth_user.views import index
import apps.profile_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', index, name='index'),
    path('accounts/profile/', include('apps.profile_user.urls'), name="profile_user") # buscas rotas do app profile_user
]

handler404 = 'apps.auth_user.views.page_not_found'
