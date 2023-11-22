from django.db import models

# Create your models here.
class signupinfo(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    address=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
    DateofBirth=models.DateField()