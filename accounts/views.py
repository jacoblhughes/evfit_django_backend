from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views import generic

from . import forms


# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

class NewProspect(CreateView):
    form_class=forms.NewProspectForm
    template_name='accounts/new_prospect.html'
    success_url = reverse_lazy('home')