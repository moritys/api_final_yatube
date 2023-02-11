from django.urls import include, path

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router_v1 = DefaultRouter()
router_v1.register(r'^posts', PostViewSet, basename='api_posts')
router_v1.register(r'^groups', GroupViewSet, basename='api_groups')
router_v1.register(r'^follow', FollowViewSet, basename='api_follow')
router_v1.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='api_comments'
)

urlpatterns = [
    path(
        'v1/jwt/create/', TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'v1/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1/', include(router_v1.urls)),
]
