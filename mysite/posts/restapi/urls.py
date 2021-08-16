from django.urls import path, include
from .views import PostViewSet, PostCommentView, PostCommentViewSet
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
# router.register(r'comments', PostCommentViewSet, basename='Commentsss')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

user_list = PostCommentViewSet.as_view({'get': 'comments'})

urlpatterns = [
    path('', include(router.urls)),
    path('post/<int:pk>/comments', user_list, name='post-comments'),
]