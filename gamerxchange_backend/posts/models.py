from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
   owner = models.ForeignKey(User, on_delete=models.CASCADE)
   title = models.CharField(max_length=100)
   uploaded_at = models.DateTimeField(auto_now_add=True)
   content = models.TextField(blank=True)
   image = models.ImageField(upload_to='images/', default='../default_post_rgq6aq', blank=True)

class Meta:
    ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.id} {self.title}'
