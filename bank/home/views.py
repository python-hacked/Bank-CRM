from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mass_mail
from django.http import JsonResponse
from django.contrib import messages
import random
from . models import *
# Create your views here.

def index(request):
    return render(request,'views/index.html')

def create_account_page(request):
    return render(request,'views/create.html')

def createaccount(request):
    if request.method=="POST":
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        reppassword=request.POST['reppassword']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        age=request.POST['age']
        id_number=request.POST['id']
        idpic=request.FILES['img']
        mailotp=request.POST['mailotp']
        Customerotp=request.POST['Customerotp']
        if mailotp==Customerotp:
            Register_user.objects.create(email=email,phone=phone,username=username,password=password,repassword=reppassword,first_name=first_name,last_name=last_name,age=age,id_number=id_number,img=idpic)
            # messages.success("user created succesfully")
            return render(request,'views/create.html')


def addemail(request):
    if request.method == "GET":
        num = random.random()
        num=num*1000000
        num=int(num)
        email = request.GET['emails']
        print(email)
        subject = 'Varification OTP '
        message = f'Hi this is your one time otp {num} thank you for registering in emailotplogin'
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list)
        msg="Otp Send Succesfull Please check Your mail"
        data={'otp':num,'msg':msg}
        return JsonResponse(data)
