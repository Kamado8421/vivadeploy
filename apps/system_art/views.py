from django.shortcuts import render
from django.http import HttpResponse
from apps.profile_user.models import InfoUser, Publication, CategoryPost
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        user = request.user

        info_user, created = InfoUser.objects.get_or_create(user=user)

        if created:
            info_user.save()

        posters = Publication.objects.all()

        return render(request, 'vivarte_pages/feed.html', {'user': user, 'info': info_user, 'posters': posters, 'search': False, 'following': None})
    
    else:
        return render(request, 'index.html')


@login_required(login_url='index')
def galery_virtual(request):
    user = request.user

    info_user, created = InfoUser.objects.get_or_create(user=user)

    if created:
        info_user.save()

    posters = Publication.objects.all()
    return render(request, 'vivarte_pages/galery_vitual.html', {'user': user, 'posters': posters, 'info': info_user})

