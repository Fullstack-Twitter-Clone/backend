from django.contrib import admin

from .models import User, Tweet # ! TODO

admin.site.register(User)
admin.site.register(Tweet)
