from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, FollowViewSet, PostViewSet


router_v1 = DefaultRouter()
router_v1.register(r'^posts', PostViewSet, basename='api_posts')
router_v1.register(r'^groups', GroupViewSet, basename='api_groups')
# router_v1.register(r'^follow', FollowViewSet, basename='api_follow')
router_v1.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='api_comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls)),
]
