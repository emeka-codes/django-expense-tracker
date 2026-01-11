from django.db import models
import datetime

# Create your models here.
class Expenses(models.Model):
    user= models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    name= models.CharField()
    product= models.CharField()
    amount= models.IntegerField()
    category= models.CharField()
    description= models.CharField()
    date= models.DateTimeField(default= datetime.date.today)
    
