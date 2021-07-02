from exerciselog.models import ExerciseInformation
from rest_framework import routers
from profiles.api.views import ProfileViewset
from tracking.api.views import EFHabitMeasViewset
from blog.api.views import EFBlogViewset
from habitposts.api.views import EFPostViewset
from habits.api.views import EFHabitViewset
from expo.api.views import ExpoRecordViewset
from exerciselog.api.views import ExerciseRecordViewset

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewset, basename = 'Profile')
router.register(r'habit_measurements', EFHabitMeasViewset, basename='HabitMeasurement')
router.register(r'blog_posts', EFBlogViewset, basename='BlogPost')
router.register(r'habit_posts', EFPostViewset, basename='HabitPost')
router.register(r'habits', EFHabitViewset, basename='Habit')
router.register(r'expo', ExpoRecordViewset, basename='Expo')
router.register(r'exerciselog', ExerciseRecordViewset, basename='ExerciseLog')
