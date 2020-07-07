from rest_framework import serializers
from .models import Like,Comment,post
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields=('id','username')

class postSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = post
        fields = ('id','user', 'caption','photo','date_created','date_updated')


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    photo= postSerializer()
    class Meta:
        model = Like
        fields = ('id','user', 'photo','date_created')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    photo= postSerializer()
    class Meta:
        model = Comment
        fields = ('id','user', 'photo','date_created','content')
