from rest_framework.routers import DefaultRouter
from .api_views import AdViewSet, ExchangeProposalViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'proposals', ExchangeProposalViewSet)

urlpatterns = router.urls
