from posts.models import Comment, Group, Follow, Post, User

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        slug_field='slug', queryset=Group.objects.all(), required=False
    )
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'author', 'image', 'group', 'pub_date',
        )


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=False, queryset=User.objects.all()
    )
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=False, queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'author',)
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'author',]
            )
        ]
