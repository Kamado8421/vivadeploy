from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def page_not_found(request, exception):
    return render(request, template_name='error404.html')


def index(request):
    if request.user.is_authenticated:
        return redirect('my_profile')
    else:
         return render(request, template_name='index.html')

