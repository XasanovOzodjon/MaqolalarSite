from django.db import models

# Create your models here.

class Teacher(models.Model):
    fullname = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teachers/', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.fullname