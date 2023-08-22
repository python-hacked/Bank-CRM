from django.shortcuts import render,redirect
from .models import Registration,Account_maintain
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
import math
import random
from django.db.models import Q
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
                numberids=id,rpassword=rpassword,idpic=idpic,account_no=acc)
            
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


def transferpage(request,pk):
    print(pk)
    data=Registration.objects.filter(Q(id=pk)).all()
    account_data=Account_maintain.objects.filter(Q(id=pk)).all()
    return render(request,'dashboard-transfer.html',{'data':data,'account_data':account_data})

def transfermoney(request):
    if request.method=="POST":
        id=request.POST['id']
        money=request.POST['money']
        money=int(money)
        accountnum=request.POST['accountnum']
        sender=Registration.objects.get(id=id)
        sender_id=sender.id
        sender_account_balance=sender.account_balance
        reciver_check=Registration.objects.filter(account_no=accountnum).exists()
        if  reciver_check is True:
            if sender_account_balance >= money:
                reciver=Registration.objects.get(account_no=accountnum)
                reciver_id=reciver.id
                reciver_accountnum_balance=reciver.account_balance
                reciver_change_balance = reciver_accountnum_balance + money
                sender_change_balance = sender_account_balance - money
                Registration.objects.filter(id=reciver_id).update(account_balance=reciver_change_balance)
                Registration.objects.filter(id=sender_id).update(account_balance=sender_change_balance)
                #history work
                sender_reamaing_amount=sender_account_balance-money
                reciver_reamaing_amount=reciver_accountnum_balance + money
                Account_maintain.objects.create(coustmer=sender,transaction_amount=money,transaction_type="Debit",account_update_balance=sender_reamaing_amount)
                Account_maintain.objects.create(coustmer=reciver,transaction_amount=money,transaction_type="Creadit",account_update_balance=reciver_reamaing_amount)
                data=Registration.objects.filter(Q(id=sender_id)).all()
                account_data=Account_maintain.objects.filter(Q(id=sender_id)).all()
                return render(request,'dashboard-transfer.html',{'data':data,'account_data':account_data})
            else:
                error="insufficent balance!"
                data=Registration.objects.filter(Q(id=sender_id)).all()
                account_data=Account_maintain.objects.filter(Q(id=sender_id)).all()
                return render(request,'dashboard-transfer.html',{'data':data,'account_data':account_data,'error':error})
        else:
                error="Account Number Is Wrong !"
                data=Registration.objects.filter(Q(id=sender_id)).all()
                account_data=Account_maintain.objects.filter(Q(id=sender_id)).all()
                return render(request,'dashboard-transfer.html',{'data':data,'account_data':account_data,'error':error})




