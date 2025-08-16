from rest_framework.routers import DefaultRouter
from .views import ThreadViewSet, MessageViewSet

router = DefaultRouter()
router.register('threads', ThreadViewSet, basename='thread')
router.register('messages', MessageViewSet, basename='message')

urlpatterns = router.urls
