from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'tweets'
        ordering = ['-created_at']
        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'

