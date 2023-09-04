from deal_handler.views import DealViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'deal', DealViewSet, basename='deals')

urlpatterns = router.urls
