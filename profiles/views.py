from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView
from django.views import generic

from django.core.mail import EmailMessage, send_mail
from django.shortcuts import redirect, reverse
from django.template.loader import get_template

from django.http import HttpResponseRedirect, HttpResponse

from . import forms
from .forms import UserCreateForm


# Create your views here.

class ProfileView(TemplateView):
    template_name = 'profiles/profile.html'

class NewProspectView(FormView):
    form_class=forms.NewProspectForm
    template_name='profiles/new_prospect.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        message = "{first_name} {last_name} - {email} said: ".format(
            first_name=form.cleaned_data.get('first_name'),
            last_name = form.cleaned_data.get('last_name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            'New Client Reach Out!',
            message,
            'jacob@evidentfitness.com',
            ['jacob@evidentfitness.com',],
            fail_silently=False,
        )
        # msg = EmailMessage('New Client Reach Out','Message 1010101010101','jacob@evidentfitness.com',['jacob@evidentfitness.com',])
        # msg.send()
        # print(msg.send())
        return HttpResponseRedirect(reverse('home'))

class SignUpView(FormView):
    form_class=forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'profiles/signup.html'
