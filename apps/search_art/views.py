from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from apps.profile_user.models import InfoUser, Publication, CategoryPost
from django.contrib.auth.decorators import login_required

@login_required(login_url='index')
def search_user(request):
    user = request.user

    info_user, created = InfoUser.objects.get_or_create(user=user)
    users = User.objects.all()

    if created:
        info_user.save()

    posters = Publication.objects.all()
    return render(request, 'vivarte_pages/search_user.html', {'user': user, 'posters': posters, 'info': info_user, 'users': users})