from django.db import models

# Create your models here.

class Login(models.Model):
    name = models.CharField(max_length=50)
    last=  models.CharField(max_length=50 ,default="")
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=14 , default="")

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=50)
    last=  models.CharField(max_length=50 , default="")
    email = models.EmailField(null=True)
    message = models.TextField(null=False)

    def __str__(self):
        return self.name