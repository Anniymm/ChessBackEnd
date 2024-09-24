from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser): 
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField() # deadline
    end_date = models.DateTimeField() # deadline
    # customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_projects')
    # contractor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contractor_projects')

    def __str__(self):
        return self.name

class Task(models.Model):  # proeqtshi arsebuli konkretuli davaleba
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=200)
    description = models.TextField()
    # start_date = models.DateTimeField()
    # end_date = models.DateTimeField()
    # status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')])

    def __str__(self):
        return self.name

class TaskStatus(models.Model): #ra donezea davaleba
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='statuses')
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')]) #aqedan shedzlebs archevas 
    responsible_person = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)  # ra drosac davalebis statusi sheicvala

class Timer(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='timer')
    customer_time = models.DurationField(default=0)
    contractor_time = models.DurationField(default=0)
    last_switched = models.DateTimeField(auto_now=True)
    current_responsible = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='current_timers')

# kavshirebi invited peoplebtan !!!!