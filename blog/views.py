from django.shortcuts import render
from . import models
from . import forms
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views import generic
from django.urls import reverse

from braces.views import SelectRelatedMixin


# Create your views here.

class BlogPostList(SelectRelatedMixin, generic.ListView):
    queryset = models.BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blogpost_list.html'
    select_related = ('author',)

class BlogPostDetail(generic.DetailView):
    model = models.BlogPost
    template_name = 'blog/blogpost_detail.html'

class CreateBlog(LoginRequiredMixin, generic.CreateView):
    fields = ("title","author", "content", "status","tags")
    model = models.BlogPost