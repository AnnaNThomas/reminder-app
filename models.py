from django.db import models

# Create your models here.
class register(models.Model):
    firstname= models.CharField(max_length=50,null=True)
    lastname= models.CharField(max_length=50,null=True)
    email= models.CharField(max_length=200,null=True)
    mobile= models.IntegerField()
    gender= models.CharField(max_length=50,null=True)
    dob= models.CharField(max_length=50,null=True)
    password= models.CharField(max_length=200,null=True)

class dt(models.Model):
    date= models.DateField(null=True)
    time= models.CharField(max_length=50,null=True)
    image = models.FileField(null=True,blank=True,upload_to = 'images/')
   