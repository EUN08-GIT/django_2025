from django.contrib.auth.models import User
from django.db import models




# Create your models here.
class Shop(models.Model):
        title = models.CharField(max_length=30)
        content = models.TextField()
        price = models.IntegerField()
        seller = models.CharField(max_length=10)

        def __str__(self):
            return f'상품이름:{self.title} -상품 설명- {self.content} -상품 가격- {self.price}'

