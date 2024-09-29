from rest_framework.routers import DefaultRouter
from .views import UserProjectsViewSet

router = DefaultRouter()
router.register(r'projects', UserProjectsViewSet, basename='user-projects')

urlpatterns = router.urls
