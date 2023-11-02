from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    mail=models.EmailField()
    ppic=models.ImageField(upload_to='image',null=True)
