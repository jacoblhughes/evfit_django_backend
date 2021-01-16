from rest_framework import routers
from accounts.api.views import ProfileViewset
from tracking.api.views import EFHabitMeasViewset
from blog.api.views import EFBlogViewset
from posts.api.views import EFPostViewset

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewset, basename = 'Profile')
router.register(r'habit_measurements', EFHabitMeasViewset, basename='HabitMeasurement')
router.register(r'blog_posts', EFBlogViewset, basename='BlogPost')
router.register(r'posts', EFPostViewset, basename='Post')
