from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main.apps.UsersConfig'

class TweetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main.apps.TweetsConfig'
    
class FollowersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main.apps.FollowersConfig'

