from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','first_name','last_name','email','password1','password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
    

class NewProspectForm(forms.Form):
    first_name=forms.CharField(max_length=255)
    last_name=forms.CharField(max_length=255)
    email=forms.EmailField(max_length=255)
    message=forms.CharField(max_length=1024, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].label = 'Message (Use the below message or create your own!)'
        self.fields['message'].initial = 'Hello, my name is [YOUR NAME] and I am ready, willing, and able to start the journey that leads to a healthier me!'
        self.fields['email'].label = 'Email Address'