from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import EventUser
from django.contrib.auth.decorators import login_required

@login_required(login_url='index')
def global_events(request):
    if request.method == 'GET':
        user = request.user

        events = EventUser.objects.all()
        my_events = EventUser.objects.filter(user=user)

        

        return render(request, 'vivarte_pages/events_global.html', {'user': user, 'events': events, 'my_events': my_events})
    elif request.method == 'POST':
        user = request.user
        event_title = request.POST.get('eventname')
        event_date = request.POST.get('eventdate')
        event_hour = request.POST.get('eventhour')
        email = request.POST.get('email')
        instagram = request.POST.get('instagram')
        whatsapp = request.POST.get('whatsapp')
        link_event = request.POST.get('link_event')
        description = request.POST.get('description')

        EventUser.objects.create(user=user,
                                 title=event_title,
                                 event_time=event_hour,
                                 description=description,
                                 email=email,
                                 whatsapp_number=whatsapp,
                                 instagram_handle=instagram,
                                 event_url=link_event,
                                 event_date=event_date)
        
        return redirect('global_events')
    
