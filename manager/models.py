from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.shortcuts import render, redirect

# Create your models here.

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    b_group = models.TextField(blank=False, null=False)
    last_donation = models.DateField()
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Models
class Donor(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')
    ]
    AVAILABILITY_STATUS = [('Available', 'Available'), ('Not Available', 'Not Available')]
    
    name = models.CharField(max_length=100)
    medical_history = models.TextField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    location = models.CharField(max_length=200)
    availability_status = models.CharField(max_length=20, choices=AVAILABILITY_STATUS)
    last_donation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.blood_group})"

class Recipient(models.Model):
    URGENCY_LEVELS = [
        ('Emergency', 'Emergency'),
        ('Within 24 Hours', 'Within 24 Hours'),
        ('Within a Week', 'Within a Week')
    ]
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')
    ]
    
    name = models.CharField(max_length=100)
    urgency_level = models.CharField(max_length=20, choices=URGENCY_LEVELS)
    location = models.CharField(max_length=200)
    blood_type_required = models.CharField(max_length=3, choices=BLOOD_GROUPS)

    def __str__(self):
        return f"{self.name} ({self.blood_type_required})"