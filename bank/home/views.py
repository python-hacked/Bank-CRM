from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mass_mail
from django.http import JsonResponse
from django.contrib import messages
import random
from . models import *
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def index(request):
    return render(request,'views/index.html')

def create_account_page(request):
    return render(request,'views/create.html')

def loginpage(request):
    return render(request,'views/login.html')

def createaccount(request):
    # try:
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
            phn=str(phone)
            age_ch=str(age)
            account_number = age_ch +phn
            check=Register_user.objects.filter(Q(username=username)).exists()
            if check is False:
                if mailotp==Customerotp:
                    if password==reppassword:
                        if len(phone)==10:
                            Register_user.objects.create(email=email,phone=phone,username=username,password=password,repassword=reppassword,first_name=first_name,last_name=last_name,age=age,id_number=id_number,img=idpic,account_number=account_number)
                            messages.error(request,"Account Created Succesfully!")
                            return render(request,'views/create.html')
                        else:
                            messages.error(request,"Phone Number is Wrong!It contains 10 Number")
                            return render(request,'views/create.html')
                    else:
                        messages.error(request,"Password mismtechd!")
                        return render(request,'views/create.html')
                else:
                    messages.error(request,"otp unmatched!")
                    return render(request,'views/create.html')
            else:
                messages.error(request,"user name already exists!")
                return render(request,'views/create.html')
            

    # except Exception as e:
    #     return render(request,'views/exceptation.html')


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

@csrf_exempt
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        check=Register_user.objects.filter(Q(username=username)).exists()
        if check is True:
            user_data = Register_user.objects.get(Q(username=username))
            user=user_data.username
            pwd=user_data.password
            id=user_data.id
            if pwd==password:
                data=Register_user.objects.filter(Q(id=id)).all()
                userdata=Register_user.objects.get(id=id)
                account_data=Account_maintain.objects.filter(Q(coustmer=userdata)).all().order_by('-id') 
                return render(request,'views/dashboard.html',{'data':data,'account_data':account_data})
            else:
                messages.error(request,"Password Mismatched!")
                return render(request,'views/login.html')
        else:
            messages.error(request,"Username Not Exists!")
            return render(request,'views/login.html')
        
def transferpage(request,pk):
    data=Register_user.objects.filter(Q(id=pk)).all()
    account_data=Account_maintain.objects.filter(Q(id=pk)).all()
    return render(request,'views/dashboard-transfer.html',{'data':data,'account_data':account_data})

def transfermoney(request):
    if request.method=="POST":
        id=request.POST['id']
        money=request.POST['money']
        money=int(money)
        accountnum=request.POST['accountnum']
        sender=Register_user.objects.get(id=id)
        sender_id=sender.id
        sender_account_balance=sender.account_balance
        reciver_check=Register_user.objects.filter(account_number=accountnum).exists()
        if  reciver_check is True:
            if sender_account_balance >= money:
                reciver=Register_user.objects.get(account_number=accountnum)
                reciver_id=reciver.id
                reciver_accountnum_balance=reciver.account_balance
                reciver_change_balance = reciver_accountnum_balance + money
                sender_change_balance = sender_account_balance - money
                Register_user.objects.filter(id=reciver_id).update(account_balance=reciver_change_balance)
                Register_user.objects.filter(id=sender_id).update(account_balance=sender_change_balance)
                #history work
                sender_reamaing_amount=sender_account_balance-money
                reciver_reamaing_amount=reciver_accountnum_balance + money
                Account_maintain.objects.create(coustmer=sender,transaction_amount=money,transaction_type="Debit",account_update_balance=sender_reamaing_amount)
                Account_maintain.objects.create(coustmer=reciver,transaction_amount=money,transaction_type="Creadit",account_update_balance=reciver_reamaing_amount)
                data=Register_user.objects.filter(Q(id=sender_id)).all()
                account_data=Account_maintain.objects.filter(Q(id=sender_id)).all()
                return render(request,'views/dashboard-transfer.html',{'data':data,'account_data':account_data})
            else:
                error="insufficent balance!"
                data=Register_user.objects.filter(Q(id=sender_id)).all()
                account_data=Account_maintain.objects.filter(Q(id=sender_id)).all()
                return render(request,'views/dashboard-transfer.html',{'data':data,'account_data':account_data,'error':error})
        else:
                error="Account Number Is Wrong !"
                data=Register_user.objects.filter(Q(id=sender_id)).all()
                account_data=Account_maintain.objects.filter(Q(id=sender_id)).all()
                return render(request,'views/dashboard-transfer.html',{'data':data,'account_data':account_data,'error':error})


def chargesim(request,pk):
    data=Register_user.objects.filter(Q(id=pk)).all()
    return render(request,'views/dashboard-chargesim.html',{'data':data})

def chargesimreal(request):
    id=request.POST.get('id')
    charge_amount=int(request.POST.get('charge'))
    Phonenum=request.POST.get('Phonenum')
    sender=Register_user.objects.get(id=id)
    sender_id=sender.id
    sender_account_balance=sender.account_balance
    if sender_account_balance >=charge_amount:
        sender_change_balance = sender_account_balance - charge_amount
        sender_reamaing_amount = sender_account_balance - charge_amount
        phone_reason="mobile recharge"
        Register_user.objects.filter(id=sender_id).update(account_balance=sender_change_balance)
        Account_maintain.objects.create(coustmer=sender,reason=phone_reason,transaction_amount=charge_amount,transaction_type="Debit",account_update_balance=sender_reamaing_amount)
        print(Phonenum,id)
        data=Register_user.objects.filter(Q(id=id)).all()
        userdata=Register_user.objects.get(id=id)
        account_data=Account_maintain.objects.filter(Q(coustmer=userdata)).all().order_by('-id') 
        return render(request,'views/dashboard.html',{'data':data,'account_data':account_data})
       
def dashbord(request):
    # user_id=id
    # print(user_id)
    return render(request,'views/dashboard.html')
        