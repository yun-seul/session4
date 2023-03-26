from django.db import models

# Create your models here.
class Blog(models. Model):
    title = models.CharField(max_length=50)
    subtitle = models.TextField(max_length=150)
    author = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    introduce = models.TextField()

    
def __str__(self):
    return self.title

