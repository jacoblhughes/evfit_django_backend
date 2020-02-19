from django.views.generic import TemplateView
from accounts.models import User
from blog.models import BlogPost
from django.urls import reverse

from django.views import generic

from braces.views import SelectRelatedMixin

from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_five'] = BlogPost.objects.filter(status=1).order_by('-created_on')[:5]
        return context

    def get_absolute_url(self):
        return reverse(
            'blog:blogpost_detail',
            kwargs = {
                'slug':self.slug,
                'pk': self.pk
            }
        )

class AboutPage(TemplateView):
    template_name = 'about.html'

class ContactPage(TemplateView):
    template_name = 'contact.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class EFAdminPage(TemplateView):
    template_name = 'efadmin.html'

# class RecentPostList(SelectRelatedMixin, generic.ListView):
#     template_name = 'recent_post_list.html'
#     select_related = ('author',)
