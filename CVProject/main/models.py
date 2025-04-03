from django.db import models


class CV(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    skills = models.CharField(max_length=255, blank=True)
    projects = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    contacts = models.TextField(blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class RequestLog(models.Model):
    class Meta:
        db_table = 'requests_logs'

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    http_method = models.CharField(max_length=255)
    path = models.TextField()
    query = models.TextField()
    ip_address = models.CharField(max_length=255)
    status = models.IntegerField()
