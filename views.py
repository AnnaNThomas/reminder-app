import email
from django.shortcuts import render, redirect
from .models import register, dt
from .forms import registerform
from django.contrib.auth import logout
from datetime import datetime, timedelta
from dateutil import parser
from django.conf import settings
import re
from django.core.mail import send_mail
# Create your views here.


def index(request):
    return render(request, 'index.html')


def reg(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        password = request.POST.get('password')

        register(firstname=firstname, lastname=lastname, email=email,
                 mobile=mobile, gender=gender, dob=dob, password=password).save()
        return redirect('login')
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')


def log(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cr = register.objects.filter(email=email, password=password)
        if cr:
            user_details=register.objects.get(email=email,password=password)
            id=user_details.id
            email=user_details.email
            request.session['id']=id
            user_email = request.session['email']=email
            return redirect('msg')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'registration.html')

def msg(request):
  if request.method=='POST':
    date=request.POST.get('date')
    time=request.POST.get('time')
    image=request.POST.get('image')
    dt(date=date,time=time,image=image).save()
    #open text file
  text_file = open("media/images/ecom.txt", "r")
  #read text file
  textdata = text_file.read()
  text_file.close()
  #fetch tomorrow date
  uemail1 = request.session['email']
  print(uemail1)
  tomorrow = datetime.now()+timedelta(1)
  tomorrow_date = tomorrow.strftime('%d-%m-%Y')
  match_date = parser.parse(textdata, fuzzy=True)
  event_date = match_date.strftime('%d-%m-%Y')
  email_from = settings.EMAIL_HOST_USER 
  #send email if event date is equals to tomorrow date
  if(tomorrow_date == event_date):
        send_mail('There is an event', textdata, email_from,
                  [uemail1], fail_silently=False)
  else:
        print("event not found")
  return render(request,'page.html')

def logoutuser(request):
    logout(request)
    return redirect('index')


def notification(request):
    return render(request, 'notification.html')
