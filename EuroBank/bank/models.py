from django.db import models


class Registration(models.Model):
    email=models.EmailField(max_length=254)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    username=models.CharField(max_length=50)
    age=models.IntegerField()
    password=models.CharField(max_length=256)
    idnumber=models.IntegerField()
    id_img=models.ImageField(upload_to='idimage')
    account_no=models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.fname