from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import InfoUser, Publication, CategoryPost
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def self_profile(request):
    if request.method == 'POST':
        user = request.user

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()

        try:
            info = get_object_or_404(InfoUser, user=user)
            info.birth = request.POST.get('age')
            info.biography = request.POST.get('biography')
            info.save()
        except InfoUser.DoesNotExist:
            pass

        return redirect('my_profile')

    elif request.method == 'GET':
        user = request.user

        info_user, created = InfoUser.objects.get_or_create(user=user)

        if created:
            info_user.save()

        posters = Publication.objects.filter(user=user)

        return render(request, 'vivarte_pages/profile.html', {'user': user, 'info': info_user, 'posters': posters, 'search': False, 'following': None})
    

def feed(request):
    return HttpResponse("seu feed")

@login_required(login_url='index')
def new_post(request):
    if request.method == 'GET':
        return render(request, 'vivarte_pages/new_post.html')
    elif request.method == 'POST':

        user = request.user

        img_post = request.POST.get('img_post')
        legend = request.POST.get('legend')

        c = CategoryPost.objects.get(id=2)

        Publication.objects.create(user=user, tag_category=c, legend=legend, url_img=img_post)

        return redirect('my_profile')