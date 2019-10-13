from django.db import models
# from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField() #标题描述
    answer = models.TextField()

    def __str__(self):
        return '热点: {}'.format(self.title)


