from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    def __str__(self):
        return f'책 제목:{self.title} -책 내용- {self.content} -책 저자- {self.author}'
