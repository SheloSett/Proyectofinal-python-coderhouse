from email.headerregistry import Address
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="profile_image/", blank=True)

    def __str__(self):
        return self.user.username + " - profile" 
    
# user = User.objects.last()
# profile = User_profile.objects.create(user=user, phone="phone", address = "address", image ="image" )