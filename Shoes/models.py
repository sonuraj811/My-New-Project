from django.db import models

# Create your models here.
class registeration_data(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    email= models.EmailField(max_length=100,null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    confirmpassword = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="Profile", null=True, blank=True)

class category_data(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    content = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="Profile", null=True, blank=True)

class product_data(models.Model):
    category = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    quantity= models.IntegerField(null=True, blank=True)
    descrption= models.CharField(max_length=100,null=True, blank=True)
    image = models.ImageField(upload_to="Profile", null=True, blank=True)

class contact_data(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField( null=True, blank=True)
    subject= models.CharField(max_length=50, null=True, blank=True)
    message= models.CharField(max_length=100,null=True, blank=True)
