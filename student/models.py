from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=100,blank=True)
    last_name=models.CharField(max_length=100,blank=True)
    email=models.EmailField(max_length=100,unique=True,blank=True)

    def __str__(self):
        return self.first_name+''+self.last_name
