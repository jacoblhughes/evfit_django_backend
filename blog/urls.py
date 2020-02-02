from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.BlogPostList.as_view(), name='all_blogposts'),
    path("create/", views.CreateBlog.as_view(), name="create"),

    path('<int:pk>/<slug:slug>/', views.BlogPostDetail.as_view(), name='blogpost_detail'),
]