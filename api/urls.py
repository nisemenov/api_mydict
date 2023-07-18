from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from api.views import (PostViewSet,
                       CommentViewSet,
                       GroupViewSet)


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet,
                basename='comments')
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

urlpatterns += [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
