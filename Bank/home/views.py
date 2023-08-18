from django.shortcuts import render,redirect
from .models import Registration
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
import math
import random
from django.conf import settings
from django.core.mail import send_mail




# Create your views here.
def index(request):
    form=Registration.objects.all()
    return render(request,'index.html', {'form': form})

def registration(request):
    if request.method=='POST':
        email=request.POST['email']
        fname=request.POST['fname']
        phone=request.POST['phone']
        lname=request.POST['lname']
        uname=request.POST['uname']
        age=request.POST['age']
        password=make_password(request.POST['password'])
        id=request.POST['id']
        rpassword=request.POST['rpassword']
        idpic=request.POST['idpic']
        if Registration.objects.filter(email=email).exists():
            return render(request, 'index.html', {'msg': 'Email Already Exists'})
        elif Registration.objects.filter(phone=phone).exists():
            return render(request, 'index.html', {'msg': 'Phone Already Exists'})
        else:
            acc=str(phone)+str(id)
            print(acc)
            otp = get_otp()
            Registration.objects.create(
                email=email, fname=fname, phone=phone, lname=lname, uname=uname, Otp=otp,age=age,password=password,
                id=id,rpassword=rpassword,idpic=idpic,account_no=acc)
            
            subject = "OTP for Verification"
            message = f"One-Time Password is: {otp}. It is valid for 3 minutes only and can be used only once for verification. Terms and conditions apply."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('/otp/')
    else:
        return HttpResponse('Email is not register')


def verifyotp(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = request.POST['otp']
        if Registration.objects.filter(email=email, Otp=otp).exists():
            user = Registration.objects.get(email=email)
            user.is_verified = True
            user.save()
            return render(request, 'login.html')
        else:
            return render(request, 'otp.html', {'msg': 'You Entered Otp Or Email Incorrect'})


def login(request):
    return render(request,'login.html')

def login_data(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if Registration.objects.filter(email=email).exists():
            user_obj = Registration.objects.get(email=email)
            user_password = user_obj.password
            if check_password(password, user_password):
                data=Registration.objects.filter(email=email).all()
                return render(request,'dashboard.html',{'data':data})
            else:
                return render(request, 'login.html', {'msg': 'Password Incorrect'})
        else:
            return render(request, 'login.html', {'msg': 'Email Incorrect'})


def get_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(5):
        OTP += digits[math.floor(random.random()*10)]
    return OTP

def create(request):
    return render(request,'create.html')

def dashboard(request):
    return render(request,'dashboard.html')

def dashboard_transfer(request):
    return render(request,'dashboard-transfer.html')

def dashboard_onlinepass(request):
    return render(request,'dashboard-onlinepass.html')

def dashboard_more(request):
    return render(request,'dashboard-more.html')

def dashboard_disable(request):
    return render(request,'dashboard-disable.html')

def dashboard_chargesim(request):
    return render(request,'dashboard-chargesim.html')

def dashboard_bill(request):
    return render(request,'dashboard-bill.html')

def otp(request):
    return render(request,'otp.html')






