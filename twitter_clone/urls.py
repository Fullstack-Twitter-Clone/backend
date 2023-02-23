"""twitter_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from main import views
import debug_toolbar # ! TODO

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), # ! TODO MAYBE FIX
    path('home/', include('main.urls')), # ! TODO
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')), # ! TODO
    
    path('__debug__/', include(debug_toolbar.urls)),
]
