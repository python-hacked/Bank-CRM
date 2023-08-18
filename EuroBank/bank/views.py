from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from . models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import random

def register(request):
    return render(request,'create.html')

def registration(request):
    if request.method == 'POST':
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['username']
        password=make_password(request.POST['password'])
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        idnumber=request.POST['id']
        idimg=request.POST['idimg']
        if Registration.objects.filter(email=email).exists():
            messages.info(request,'email already registered')
            return redirect('/')
        elif Registration.objects.filter(phone=phone).exists():
             messages.info(request,'phone number already registered')
             return redirect('/')
        elif Registration.objects.filter(idnumber=idnumber).exists():
             messages.info(request,'id number already registered')
             return redirect('/')
        else:
            acc=str(phone)+str(idnumber)
            print(acc)
            Registration.objects.create(email=email,phone=phone,username=username,password=password,
                                        fname=fname,lname=lname,age=age,idnumber=idnumber,id_img=idimg,account_no=acc)
            otp=random.randint(1000,9999)
            request.session['otp']=otp
            subject = 'verify your otp '
            message = f'mail sucessfully send otp:- {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request,f'otp sent successfully')
            return redirect('verifyotp')
    return render(request,'create.html')

def userlogin(request):
    return render(request,'login.html')

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        user_password = request.POST["password"]
        if Registration.objects.filter(email=email).exists():
            obj = Registration.objects.get(email=email)
            password = obj.password
            if check_password(user_password, password):
                return redirect('dashboard/')
            else:
                messages.success(request,f"invalid password")
                return redirect("userlogin")
        else:
            messages.success(request,f"email not registered")
            return redirect('userlogin')
    return render(request,'login.html')

def dashboard(request):
    user=Registration.objects.all()
    return render(request,'dashboard.html',{'user':user})

def verifyotp(request):

    return render(request,'verify-otp.html')


def verify(request):
    if request.method == 'POST':
        otp2 = request.POST.get('otp0')
        otp1 = request.session.get('otp')

        a = str(otp2)
        b = str(otp1)
        if a == b:
           
            return redirect('dashboard')
        else:
            messages.error(request,'invalid otp please enter valid otp ')
            return redirect('verifyotp')
    else:
       return redirect('verifyotp')