from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'profiles'

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    # path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('joinef/', views.NewProspectView.as_view(), name = 'new_prospect' ),
    # path('change-password/', auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset_form.html'), name='change-password'),
    # path('change-password-confirm/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # path('change-password-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),


]
