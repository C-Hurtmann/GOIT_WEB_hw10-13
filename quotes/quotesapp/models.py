from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    class Meta: # Really need it?
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
            ]
    
    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    fullname = models.CharField(max_length=100, null=False, unique=True)
    born_date = models.DateField(null=False)
    born_location = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f'{self.fullname}'
    
    def get_absolute_url(self):
        return reverse("quotesapp:author_detail", kwargs={'author_id': self.pk})


class Quote(models.Model):
    quote = models.TextField(max_length=500, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='quotes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f'{self.quote}'