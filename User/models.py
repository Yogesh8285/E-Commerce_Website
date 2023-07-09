from django.db import models
from Admin.models import UserInfo,Product
from datetime import datetime
# Create your models here.

class MyCart(models.Model):
    user = models.ForeignKey(to='Admin.UserInfo', 
              on_delete=models.CASCADE)
    prod = models.ForeignKey(to='Admin.Product', 
               on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table  = "MyCart"

class OrderMaster(models.Model):
    user = models.ForeignKey(to='Admin.UserInfo', 
              on_delete=models.CASCADE)
    amount = models.FloatField(default=1000)
    qty = models.IntegerField()
    details = models.CharField(max_length=200)
    ordertime = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table  = "OrderMaster"

class Address(models.Model):
    user = models.ForeignKey(to='Admin.UserInfo',on_delete=models.CASCADE)
    name = models.CharField(max_length=30 ,default="")
    mono = models.IntegerField()
    house = models.CharField(max_length=30,default="")
    pin = models.IntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)

    class Meta:
        db_table = "Address"
        
class Account(models.Model):
    user = models.ForeignKey(to='Admin.UserInfo',on_delete=models.CASCADE)
    name = models.CharField(max_length=30 ,default="")
    mono = models.IntegerField()
    house = models.CharField(max_length=30,default="")
    pin = models.IntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)

    class Meta:
        db_table = "Account"

class Myorder(models.Model):
    user = models.CharField(max_length=20)
    prod = models.ForeignKey(to='Admin.Product', 
               on_delete=models.CASCADE)
    qty = models.IntegerField()
    amount = models.IntegerField(default=100)

    class Meta:
        db_table  = "Myorder"
