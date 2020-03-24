from rest_framework import routers
from accounts import api_views as accounts_apiviews

router = routers.DefaultRouter()
router.register(r'efusers', accounts_apiviews.EFUsersViewset)
