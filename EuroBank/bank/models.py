from django.db import models


class Registration(models.Model):
    email=models.EmailField(max_length=254)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.IntegerField()
    username=models.CharField(max_length=50)
    age=models.IntegerField()
    password=models.CharField(max_length=50)
    idnumber=models.IntegerField()
    id_img=models.ImageField(upload_to='idimage')

    def __str__(self) -> str:
        return self.fname