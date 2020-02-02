from django import forms

from . import models


class BlogPostForm(forms.ModelForm):
    class Meta:
        fields = ("title", "content",'status','tags')
        model = models.BlogPost


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        