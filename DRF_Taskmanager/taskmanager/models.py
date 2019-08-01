from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', unique=True)
    MANAGER = 'Manager'
    DEVELOPER = 'Developer'
    Roles = (
        (MANAGER, 'Manager'),
        (DEVELOPER, 'Developer'),
    )
    role = models.CharField(verbose_name='Role', choices=Roles, max_length=20,)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '  Users'


class Project(models.Model):
    title = models.CharField(verbose_name='Title', unique=True, max_length=64)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'projects', blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = ' Projects'


class Task(models.Model):
    title = models.CharField(verbose_name='Title', max_length=64)
    description = models.TextField(verbose_name='Description', max_length=200)
    due_date = models.DateField()
    project = models.ForeignKey(Project, related_name = 'tasks', blank=True, null=True, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name = 'task', blank=True, null=True, on_delete=models.SET_NULL)
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Tasks'
