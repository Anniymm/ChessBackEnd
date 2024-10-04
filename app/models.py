from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from rest_framework import settings 
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model() 

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField() # deadline
    end_date = models.DateTimeField() # deadline
    # question = models.CharField(max_length=300, blank=True, null=True)
    # question_file = models.FileField(upload_to='uploads/', blank=True, null=True)
    customers = models.ManyToManyField(User, related_name='customer_projects')
    contractors = models.ManyToManyField(User,related_name='contractor_projects')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# @receiver(post_save, sender=Project)
# def send_project_question_email(sender, instance, **kwargs):
#     is_new_question = instance.question or instance.question_file
#     if is_new_question:
#         # email adresebis aghdegena 
#         customer_emails = list(instance.customers.values_list('email', flat=True))
#         contractor_emails = list(instance.contractors.values_list('email', flat=True))

#         participants = customer_emails + contractor_emails
#         # esenic iyos debugingistvis 
#         # print("Customer Emails:", customer_emails)  
#         # print("Contractor Emails:", contractor_emails)  
#         # print(f"Participants: {participants}")  

#         if participants:
#             subject = f'New Question Added in Project: {instance.name}'
#             message = f'A new question has been added to the project "{instance.name}".'
#             if instance.question:
#                 message += f'\nQuestion: {instance.question}'

#             email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, participants)

#             if instance.question_file:
#                 email.attach_file(instance.question_file.path)
#             email.send(fail_silently=False)

#             # try:  # es mqondes debugingistvis
#             #     email.send(fail_silently=False)
#             # except Exception as e:
#             #     print(f"Email failed to send: {e}")


class Task(models.Model):  # proeqtshi arsebuli konkretuli davaleba
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=200)
    description = models.TextField()
    # start_date = models.DateTimeField()
    # end_date = models.DateTimeField()
    # status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'
    question = models.CharField(max_length=300, blank=True, null=True)  # Task-level question
    question_file = models.FileField(upload_to='uploads/tasks/', blank=True, null=True)  # Task-level question file
    # customers_task = models.ManyToManyField(User, related_name='customer_projects')
    # contractors_task = models.ManyToManyField(User,related_name='contractor_projects')


    def __str__(self):
        return self.name

@receiver(post_save, sender=Task)
def send_task_question_email(sender, instance, **kwargs):
    is_new_question = instance.question or instance.question_file
    if is_new_question:
        project = instance.project
        customer_emails = list(project.customers.values_list('email', flat=True))
        contractor_emails = list(project.contractors.values_list('email', flat=True))
        participants = customer_emails + contractor_emails

        if participants:
            subject = f'New Question Added in Task: {instance.name} (Project: {project.name})'
            message = f'A new question has been added to the task "{instance.name}" in project "{project.name}".'
            if instance.question:
                message += f'\nQuestion: {instance.question}'
            
            email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, participants)

            if instance.question_file:
                email.attach_file(instance.question_file.path)
            email.send(fail_silently=False)


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