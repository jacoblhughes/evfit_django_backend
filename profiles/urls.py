from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'profiles'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('joinef/', views.NewProspectView.as_view(), name = 'new_prospect' ),


]
