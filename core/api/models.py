from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name
    

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'), 
        ('published', 'Published'),
    )
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=250)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default='published')
    slug = models.SlugField(max_length=150)
    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
    


