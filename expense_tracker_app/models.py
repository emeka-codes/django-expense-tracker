from django.db import models
import datetime

# Create your models here.
class Expenses(models.Model):
    name= models.CharField()
    product= models.CharField()
    amount= models.IntegerField()
    category= models.CharField()
    description= models.CharField()
    date= models.DateTimeField(default= datetime.date.today)
    
