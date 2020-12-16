from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=100);
    gender=models.CharField(max_length=100);
    salary=models.CharField(max_length=100);
    phone_number=models.CharField(max_length=100);
    Emp_address=models.CharField(max_length=100);

