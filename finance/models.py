from django.db import models
from user.models import *
from django.utils.timezone import now


class Transaction(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    type = models.CharField(max_length=10,default=now)
    sname = models.CharField(max_length=20)
    discription = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    date = models.DateField(default = now)


class Expense(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    category = models.CharField(max_length=10,default=now)
    discription = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    date = models.DateField(default = now)



class Bookings(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    checkin = models.DateField(default = now,null=True)
    checkout = models.DateField(default = now,null=True)
    noad = models.CharField(max_length=20)
    nokid = models.CharField(max_length=20)
    booking = models.CharField(max_length=20)
    food = models.CharField(max_length=20)
    name = models.CharField(max_length=20,default = now,)
    email = models.CharField(max_length=20,default = now)
    phon = models.CharField(max_length=20,default = now,)