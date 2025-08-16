from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProposalViewSet, ContractViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='project')
router.register('proposals', ProposalViewSet, basename='proposal')
router.register('contracts', ContractViewSet, basename='contract')

urlpatterns = router.urls
