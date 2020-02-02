from django.urls import path

from . import views

app_name = 'habits'

urlpatterns = [
    path("", views.ListHabits.as_view(), name="all"),
    path("new/", views.CreateHabit.as_view(), name="create"),
    path("posts/in/<slug>/",views.SingleHabit.as_view(),name="single"),
    path("join/<slug>/",views.JoinHabit.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveHabit.as_view(),name="leave"),
]

# urlpatterns = [
#     url(r"^$", views.ListGroups.as_view(), name="all"),
#     url(r"^new/$", views.CreateGroup.as_view(), name="create"),
#     url(r"^posts/in/(?P<slug>[-\w]+)/$",views.SingleGroup.as_view(),name="single"),
#     url(r"join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
#     url(r"leave/(?P<slug>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),
# ]
