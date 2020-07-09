from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from rest_framework import routers
from posts.views import CommentViewSet, LikeViewSet, postViewSet

router = routers.DefaultRouter()

router.register(r'posts', postViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
