"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .router import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name = 'home'),
    path('about/', views.AboutPage.as_view(), name = 'about'),
    path('contact/', views.ContactPage.as_view(), name = 'contact'),
    path('profiles/', include('profiles.urls', namespace ='profiles')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('thanks/', views.ThanksPage.as_view(), name = 'thanks'),
    path('habits/', include('habits.urls', namespace ='habits')),
    path('habitposts/', include('habitposts.urls', namespace ='habitposts')),
    path('efadmin/', views.EFAdminPage.as_view(), name = 'efadmin'),
    path('tracking/', include('tracking.urls', namespace ='tracking')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('privacy/', views.PrivacyPage.as_view(), name = 'privacy'),
    path('exerciselog/', include('exerciselog.urls', namespace ='exerciselog')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)