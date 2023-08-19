from django.db import models

# Create your models here.

class Register_user(models.Model):
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    repassword=models.CharField(max_length=20)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    id_number=models.CharField(max_length=50)
    account_number=models.CharField(max_length=25)
    account_balance=models.IntegerField(default=0)
    img=models.ImageField(upload_to='pics')
    def __str__(self) -> str:
        return self.email
    
class Account_maintain(models.Model):
    coustmer=models.ForeignKey(Register_user,on_delete=models.CASCADE)
    transaction_amount=models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    transaction_type=models.CharField(max_length=100)
    account_update_balance=models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.coustmer.username

