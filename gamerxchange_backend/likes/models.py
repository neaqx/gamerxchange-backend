from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} liked {self.post}'