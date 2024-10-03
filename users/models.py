from django.db import models
from django.contrib.auth.models import User

class PersonalSpace(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personal_space') # onetoone field, ert users erti personal space 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to='profile/', default='profile/profile_pic.jpg', blank=True)
    
    def __str__(self):
        return f"Personal Space of {self.user.user}"