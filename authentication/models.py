from django.db import models
# Create your models here.

class Contact(models.Model):
    name =models.CharField(max_length=200)
    mail = models.EmailField()
    number = models.CharField(max_length=10)
    message = models.TextField()
    def __str__(self):
        return self.name
    
class Advice(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    number = models.CharField(max_length=10)
    message = models.TextField()
    def __str__(self):
        return self.name
