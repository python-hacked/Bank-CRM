from django.db import models

# Create your models here.
class Registration(models.Model):
    email=models.EmailField( max_length=254,unique=True)
    fname=models.CharField( max_length=50)
    phone=models.CharField( max_length=50,unique=True)
    lname=models.CharField( max_length=50)
    uname=models.CharField (max_length=50)
    age=models.CharField( max_length=50)
    password=models.CharField( max_length=500)
    id=models.IntegerField(primary_key=True)
    rpassword=models.CharField( max_length=50)
    idpic=models.ImageField(upload_to='idimg/')
    Otp = models.CharField(max_length=10)


    def __str__(self) -> str:
        return self.uname