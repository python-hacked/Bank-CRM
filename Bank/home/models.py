from django.db import models

# Create your models here.
class Registration(models.Model):
    numberids=models.CharField( max_length=50)
    email=models.EmailField( max_length=254,unique=True)
    fname=models.CharField( max_length=50)
    phone=models.CharField( max_length=50,unique=True)
    lname=models.CharField( max_length=50)
    uname=models.CharField (max_length=50)
    age=models.CharField( max_length=50)
    password=models.CharField( max_length=500)
    rpassword=models.CharField( max_length=500)
    idpic=models.ImageField(upload_to='idimg/')
    Otp = models.CharField(max_length=10)
    account_no=models.CharField( max_length=16)
    account_balance=models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.uname

class Account_maintain(models.Model):
    coustmer=models.ForeignKey(Registration,on_delete=models.CASCADE)
    transaction_amount=models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    transaction_type=models.CharField(max_length=100)
    account_update_balance=models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.coustmer.uname