from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from apps.profile_user.models import InfoUser, Publication, CategoryPost
from django.contrib.auth.decorators import login_required

@login_required(login_url='index')
def chats(request):
    return render(request, 'vivarte_pages/chat.html')


@login_required(login_url='index')
def groups(request):
    return render(request, 'vivarte_pages/groups.html')
