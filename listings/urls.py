from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import HelloAPIView

app_name = 'listings'

router = DefaultRouter()
# Add routes here as needed

urlpatterns = router.urls + [
    path('hello/', HelloAPIView.as_view(), name='hello'),
] 