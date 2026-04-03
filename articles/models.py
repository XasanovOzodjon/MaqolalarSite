from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    literature = models.TextField(null=True, blank=True)

    pdf = models.FileField(upload_to='articles/pdfs/', null=True, blank=True)
    image = models.ImageField(upload_to='articles/images/', null=True, blank=True)

    author = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)

    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title