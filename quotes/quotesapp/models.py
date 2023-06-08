from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)
    
    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    fullname = models.CharField(max_length=50, null=False, unique=True)
    born_date = models.DateField(null=False)
    born_location = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return f'{self.fullname}'


class Quote(models.Model):
    quote = models.TextField(max_length=500, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f'{self.quote}'