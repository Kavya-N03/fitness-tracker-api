from django.db import models
from django.contrib.auth.models import AbstractUser

""" 
Custom User 
"""
class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ]
    profile_photo = models.ImageField(upload_to='profile_photo/',null=True,blank=True,help_text="Upload a profile picture")
    age = models.PositiveIntegerField(null=True,blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=20)
    weight = models.FloatField(null=True,blank=True,help_text="Weight in kg")
    height = models.FloatField(null=True,blank=True,help_text="Height in cm")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    
    @property
    def bmi(self):
        if self.weight and self.height and self.height>0:
            return round(self.weight/((self.height/100)**2),2)
        return None
    
