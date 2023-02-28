from django.contrib import admin

from .models import User, Tweet, Follower # ! TODO

admin.site.register(User)
admin.site.register(Tweet)
admin.site.register(Follower)
