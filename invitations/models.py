from django.db import models
from django.contrib.auth.models import User

####mowvevaaaa
class Invitation(models.Model):
    inviter = models.ForeignKey(User, on_delete=models.CASCADE)
    invitee_email = models.EmailField()
    token = models.CharField(max_length=100, unique=True)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('contractor', 'Contractor'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"Invitation from {self.inviter.username} to {self.invitee_email}"