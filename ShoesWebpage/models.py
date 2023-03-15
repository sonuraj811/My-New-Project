from django.db import models

# Create your models here.
class customerdetails(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    password  = models.CharField(max_length=100,null=True,blank=True)
    confirmpassword = models.CharField(max_length=100,null=True,blank=True)

class cartdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    size=models.IntegerField(null=True,blank=True)
    total=models.IntegerField(null=True,blank=True)