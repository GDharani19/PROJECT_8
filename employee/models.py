from django.db import models

# Create your models here.


class employee(models.Model):
    eid=models.SmallAutoField(primary_key=True)
    name=models.CharField(max_length=75)
    phone=models.PositiveBigIntegerField(unique=True)          # remove field
    employee_email=models.EmailField(max_length=254,unique=True)    # rename and add constraints
    age=models.IntegerField()              # remove constraints
    salary=models.IntegerField()   # new field