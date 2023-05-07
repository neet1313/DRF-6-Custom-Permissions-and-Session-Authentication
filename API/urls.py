from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API import views

router = DefaultRouter()
router.register('api', views.StudentViewset)

urlpatterns = [
    path('', include(router.urls))
]
