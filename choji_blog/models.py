import uuid
from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(default='Dope eh')
    active = models.BooleanField(default=True)
    author = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now=True)
    choji_code = models.UUIDField(editable=False, default=uuid.uuid4)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})


class Chapter(models.Model):
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    description = models.TextField(default='description')
    choji_code = models.UUIDField(editable=False, default=uuid.uuid4)

