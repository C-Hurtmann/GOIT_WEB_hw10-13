from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)


class Note(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150, null=False)
    