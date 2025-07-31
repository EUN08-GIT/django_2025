from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True,
                                        null=True)
    updated_date = models.DateTimeField(auto_now=True,
                                        null=True)
    uploaded_img = models.ImageField(upload_to='media/',
                                     blank=True)
    uploaded_file = models.FileField(upload_to='file/',
                                     blank=True)

    def __str__(self):
        return f'게시글 제목:{self.title} -게시글 내용- {self.content}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

