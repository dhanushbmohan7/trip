from django.db import models

# Create your models here.
class profiles(models.Model):
    name=models.CharField(max_length=10,default='')
    amount_paid=models.IntegerField(default=0)
    amount_balance=models.IntegerField(default=0)
    tableclass=models.CharField(max_length=20,default='table-active')
    def __str__(self):
        return self.name
