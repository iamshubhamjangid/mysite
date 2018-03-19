from rest_framework import routers
from django.conf.urls import url, include
from . import views


router = routers.DefaultRouter()
router.register(r'polls', views.UserViewSet)
router.register(r'choices', views.GroupViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),
]
