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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from main import views
import debug_toolbar


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet) #! TODO FIX

urlpatterns = [
    path('', include('main.urls')), # ! TODO MAYBE FIX
    path('home/', include('main.urls')), # ! TODO
    path('accounts/', include('django.contrib.auth.urls')), # ! TODO
    path('admin/', admin.site.urls),
    
    # API Endpoint URLs
    path('users/', views.UserView.as_view(), name='users'),
    path('tweets/', views.TweetView.as_view(), name='tweets'),
    
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
