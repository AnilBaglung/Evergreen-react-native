from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ContactViewSet

router = DefaultRouter()


router.register('user', UserViewSet,basename="user")
router.register('contact',ContactViewSet,basename="contact")

urlpatterns = [
    path('', include(router.urls)),
]
