from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .models import Notification
from .models import Notification1


# Create your views here.


def show_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    return render_to_response('notification.html', {'notification': n})


def delete_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    return HttpResponseRedirect('/app1/owner_profile/')


def notify(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_no = request.POST.get('contact_no')
        address = request.POST.get('address')
        o_id = request.POST.get('uname')

        n = Notification1()
        n.owner = o_id
        n.name = name
        n.contact_no = contact_no
        n.address = address
        n.save()
    return render(request, 'booking.html')
