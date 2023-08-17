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
    img=models.ImageField(upload_to='pics')
    def __str__(self) -> str:
        return self.email