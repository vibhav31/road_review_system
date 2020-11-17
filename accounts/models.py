from django.db import models

# Create your models here.
GENDER = (('Male','Male'),('Female','Female'),('Others','Others'))
class UserProfile(models.Model):
    name            = models.CharField(max_length = 80)
    email           = models.EmailField(max_length = 100,unique = True)
    phone_number    = models.CharField(max_length = 10,unique = True)
    gender          = models.CharField(max_length =10,choices=GENDER)
    date            = models.DateTimeField(auto_now_add= True)
    password        = models.CharField(max_length=15)
    confirm_password= models.CharField(max_length=15)

    def __str__(self):
        return self.email

class GuestEmail(models.Model):
    email    =models.EmailField()
    active   =models.BooleanField(default=True)
    update   =models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email