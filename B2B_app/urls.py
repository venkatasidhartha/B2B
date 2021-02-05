from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodViewset,dashboard,OrderViewset


router = DefaultRouter()
router.register('food',FoodViewset, basename='food')
router.register('clientorder',OrderViewset, basename='clientorder')

urlpatterns = [
    path('api/',include(router.urls)),
    path('',dashboard),

]