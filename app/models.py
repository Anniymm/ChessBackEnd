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
    customers = models.ManyToManyField(User, related_name='customer_projects')
    contractors = models.ManyToManyField(User,related_name='contractor_projects')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_created')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Task(models.Model):  # proeqtshi arsebuli konkretuli davaleba
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created')

    def __str__(self):
        return self.name


class Question(models.Model):  # Independent question model
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=300, blank=True, null=True)
    question_file = models.FileField(upload_to='uploads/questions/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question for Task: {self.task.name}"

@receiver(post_save, sender=Question)
def send_question_email(sender, instance, **kwargs):
    if instance.question_text or instance.question_file:
        project = instance.project
        # timer ro gachedres aqaa eg logika
        if hasattr(project, 'timer'):
            timer = project.timer
            now = timezone.now()
            time_spent = now - timer.last_switched
            
            if timer.current_responsible in project.customers.all():
                timer.customer_time += time_spent
            elif timer.current_responsible in project.contractors.all():
                timer.contractor_time += time_spent
            
            timer.last_switched = now
            timer.save()

        customer_emails = list(project.customers.values_list('email', flat=True))
        contractor_emails = list(project.contractors.values_list('email', flat=True))
        participants = customer_emails + contractor_emails

        if participants:
            subject = f'New Question Added in Project: {project.name}'
            message = f'A new question has been added to the project "{project.name}".'
            if instance.question_text:
                message += f'\nQuestion: {instance.question_text}'

            email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, participants)
            
            if instance.question_file:
                email.attach_file(instance.question_file.path)
            email.send(fail_silently=False)


class TaskStatus(models.Model): #ra donezea davaleba
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='statuses')
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')]) #aqedan shedzlebs archevas 
    responsible_person = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)  # ra drosac davalebis statusi sheicvala
# aqedean timestamp undaa amovigho rom davitvalo mere 

class Timer(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='timer')
    customer_time = models.DurationField(default=0)
    contractor_time = models.DurationField(default=0)
    last_switched = models.DateTimeField(auto_now=True)
    current_responsible = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='current_timers')

    def switch_responsibility(self, new_responsible):
        now = timezone.now()

        time_spent = now - self.last_switched

        if self.current_responsible in self.project.customers.all():
            self.customer_time += time_spent
        elif self.current_responsible in self.project.contractors.all():
            self.contractor_time += time_spent

        self.current_responsible = new_responsible
        self.last_switched = now
        self.save()

    def __str__(self):
        return f"Timer for Project: {self.project.name}"