from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def self_profile(request):
    return HttpResponse("seu perfil")

def feed(request):

    return HttpResponse("seu feed")