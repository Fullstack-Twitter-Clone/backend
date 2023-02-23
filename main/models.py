from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'followers'
        ordering = ['-user']
        verbose_name = 'Follower'
        verbose_name_plural = 'Followers'


class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_user')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    
    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'followings'
        ordering = ['-user']
        verbose_name = 'Following'
        verbose_name_plural = 'Followings'


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
