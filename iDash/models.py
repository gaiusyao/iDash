from django.db import models
from django.contrib.auth.models import User


# Blog 分类
class Category(models.Model):
    name = models.CharField(max_length=100)


# Blog 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)


# Blog 文章
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)