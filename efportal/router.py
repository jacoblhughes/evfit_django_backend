from rest_framework import routers
from accounts.api.views import ProfileViewset
from tracking.api.views import EFHabitMeasViewset

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewset, basename = 'Profile')
router.register(r'habit_measurements', EFHabitMeasViewset, basename='HabitMeasurement')

