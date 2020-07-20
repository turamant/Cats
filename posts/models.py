from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='img/')
    url = models.SlugField(max_length=200, unique=True)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug':self.url})

    def get_update_url(self):
        return reverse('post_update', kwargs={'slug':self.url})

    def get_delete_url(self):
        return reverse('post_delete', kwargs={'slug':self.url})


class Tag(models.Model):
    title = models.CharField(max_length=50)
    url = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.url})

    def get_update_url(self):
        return reverse('tag_update', kwargs={'slug':self.url})

    def get_delete_url(self):
        return reverse('tag_delete', kwargs={'slug': self.url})
