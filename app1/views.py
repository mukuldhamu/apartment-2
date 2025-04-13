# from django.shortcuts import render

# Create your views here.
from app1.models import Property_details1, BuyUpdate, Contact_us
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponseRedirect, BadHeaderError
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.template.defaulttags import csrf_token
from notifications.models import Notification
from notifications.models import Notification1
from .forms import ContactForm
from django.views.generic import View


# Create your views here.

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        pop = Contact_us()
        pop.name = name
        pop.email = email
        pop.subject = subject
        pop.message = message
        pop.save()
        return render(request, 'home.html')
    else:
        return render(request, 'home.html')


def successView(request):
    return HttpResponse('Success ! Thank you for your message.')


def header(request):
    return render(request, 'header.html', )


def footer(request):
    return render(request, 'footer.html', )


def about(request):
    return render(request, 'about.html', )


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        psw = request.POST['psw']
        user = auth.authenticate(username=email, password=psw)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def login1(request):
    if request.method == 'POST':
        email = request.POST['email']
        psw = request.POST['psw']
        user = auth.authenticate(username=email, password=psw)
        if user is not None:
            auth.login(request, user)
            return redirect('owner_profile')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login1')
    else:
        return render(request, 'login1.html')


def login2(request):
    if request.method == 'POST':
        email = request.POST['email']
        psw = request.POST['psw']
        user = auth.authenticate(username=email, password=psw)
        if user is not None:
            auth.login(request, user)
            return redirect('/app1/send_request/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login2.html')
    else:
        return render(request, 'login2.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':

        first_name = request.POST['first_name'].lower()
        last_name = request.POST['last_name'].lower()
        email = request.POST['email']
        psw = request.POST['psw']
        conf_psw = request.POST['conf_psw']
        if psw == conf_psw:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(email=email, password=psw, username=email, first_name=first_name,
                                                last_name=last_name)
                user.save()
                return render(request, 'login.html')
        else:
            messages.info(request, 'password not matching..')
            # return redirect('signup')
        return redirect('/')
    else:
        return render(request, 'signup.html')


def owner_signup(request):
    return render(request, '/app1/owner_signup/', )


def search(request):
    if request.method == 'POST':
        state = request.POST.get('state').lower()
        city = request.POST.get('city').lower()
        range = request.POST.get('price_range').lower()
        flat_type = request.POST.get('flat_type').lower()
        possession = request.POST.get('possession').lower()

        results = Property_details1.objects.filter(
            Q(state=state) or Q(city=city) or Q(flat_type=flat_type) or Q(possession=possession) or Q(
                price_range=range))
        return render(request, 'search_output.html', {'result': results})

    else:
        return render(request, 'search.html')


def tips(request):
    return render(request, 'tips.html', )


def privacy(request):
    return render(request, 'privacy.html', )


def owner_profile(request):
    n = Notification.objects.filter(user=request.user, viewed=False)
    c = Notification1.objects.all()

    return render(request, 'owner_profile.html', {'notifications': n, 'notifications1': c })


def search_output(request):
    return render(request, 'search_output.html', )


# For booking Apartment
def booking(request):
    return render(request, 'booking.html', )


# for adding property_details
def property_details(request):
    if request.method == 'POST':
        img = request.POST.get('img')
        email = request.POST.get('email')
        uname = request.POST.get('uname').lower()
        state = request.POST.get('state').lower()
        city = request.POST.get('city').lower()
        price_range = request.POST.get('price_range').lower()
        flat_type = request.POST.get('flat_type').lower()
        possession = request.POST.get('possession').lower()
        first_name = request.POST.get('first_name').lower()
        last_name = request.POST.get('last_name').lower()
        contact_no = request.POST.get('contact_no').lower()
        description = request.POST.get('description').lower()

        prop = Property_details1()
        prop.img = img
        prop.email = email
        prop.uname = uname
        prop.first_name = first_name
        prop.last_name = last_name
        prop.city = city
        prop.contact_no = contact_no
        prop.description = description
        prop.flat_type = flat_type
        prop.price_range = price_range
        prop.possession = possession
        prop.state = state

        prop.save()
        appt = Property_details1.objects.filter(uname=uname)

        return render(request, 'owner_profile.html', {'result': appt})
    else:
        return render(request, 'property_details.html')


# 9888040768
#

def update(request):
    if request == 'POST':
        email = request.POST['email']
        psw = request.POST['psw']
        conf_psw = request.POST['conf_psw']

        if psw == conf_psw:
            User.objects.filter(email=email).update()
            return HttpResponse('password updated')
        else:
            return HttpResponse('password and confirm password are not same')
    return redirect\
        ('/app1/change_password/')


# for details
def change_password(request):
    return redirect('change_password')

def send_request(request):
    return render(request, 'notif.html')

def approve(request):
    return render(request, 'approve.html')