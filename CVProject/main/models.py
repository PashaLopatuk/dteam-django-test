from django.db import models

# Create your models here.

class CV(models.Model):
    id = models.AutoField(primary_key=True)
    firstname  = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    skills = models.CharField(max_length=255, blank=True)
    projects = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    contacts = models.TextField(blank=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
