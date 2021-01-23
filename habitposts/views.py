from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(SelectRelatedMixin, generic.ListView):
    model = models.HabitPost
    select_related = ("user", "habit")


class UserPosts(generic.ListView):
    model = models.HabitPost
    template_name = "habitposts/habituser_post_list.html"

    def get_queryset(self):
        try:
            self.habitpost_user = User.objects.prefetch_related("habituser").get(
                username__iexact=self.kwargs.get("username")
            )
            print(self.habitpost_user)
        except User.DoesNotExist:
            raise Http404
        else:
            return self.habitpost_user.habituser.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["habitpost_user"] = self.habitpost_user
        return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.HabitPost
    select_related = ("user", "habit")
    template_name = "habitposts/habitpost_detail.html"


    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ('habit','message')
    model = models.HabitPost

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.HabitPost
    select_related = ("user", "habit")
    success_url = reverse_lazy("habitposts:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
