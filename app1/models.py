from django.db import models

# Create your models here.


class student(models.Model):
    sid=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()
    marks=models.PositiveIntegerField()

# NUMBER FIELDS
class numbermodel(models.Model):
    num1=models.IntegerField()
    num2=models.PositiveSmallIntegerField()
    num3=models.PositiveIntegerField()
    num4=models.PositiveBigIntegerField()
    num5=models.FloatField()
    num6=models.DecimalField(max_digits=5,decimal_places=3)
    num7=models.GenericIPAddressField()

# CHARACTER FIELDS
class charmodel(models.Model):
    char1=models.CharField(max_length=50)    
    char2=models.EmailField()
    char3=models.GenericIPAddressField()
    char4=models.SlugField()
    char5=models.TextField(max_length=500)
    char6=models.JSONField()
    char7=models.URLField(max_length=200)
    char8=models.UUIDField()

# DATE FIELDS
class datemodels(models.Model):
    date1=models.DateField()
    date2=models.TimeField()
    date3=models.DateTimeField()
    date4=models.DurationField()


# FILE FIELDS
class filemodels(models.Model):
    file1=models.FileField()
    file2=models.ImageField()
    file3=models.FilePathField()

# BOOLEAN FIELDS
class boolmodels(models.Model):
    bool1=models.BooleanField()
    bool2=models.BinaryField()

# CONSTRAINT FIELDS
class constraints(models.Model):
    sid=models.BigAutoField(primary_key=True)
    phone=models.PositiveBigIntegerField(unique=True)
    age=models.PositiveSmallIntegerField(null=True)
    gender=models.CharField(max_length=10,default='Male')
    subject=models.CharField(max_length=50,choices=[['python','python'],['django','django']])
    student=models.ForeignKey(student,on_delete=models.CASCADE)




