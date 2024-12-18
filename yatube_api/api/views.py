from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group, Post
from .mixins import CreateListViewSet, ListRetrieveViewSet
from .permissions import ReadOnlyOrAuthor
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """View для обработки всех типов запросов с публикациями"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (ReadOnlyOrAuthor,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ListRetrieveViewSet):
    """View для обработки GET запроса с группами"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (ReadOnlyOrAuthor,)


class CommentViewSet(viewsets.ModelViewSet):
    """View для обработки всех типов запросов с комментариями"""
    serializer_class = CommentSerializer
    permission_classes = (ReadOnlyOrAuthor,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(CreateListViewSet):
    """View для обработки POST и GET list запросов с подписками
    Только для аутентифицированных пользователей
    """
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        new_queryset = self.request.user.follower.all()
        return new_queryset

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(user=current_user)
