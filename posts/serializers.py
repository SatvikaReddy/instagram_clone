from rest_framework import serializers
from .models import Like,Comment,post
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.Serializer):
    #user = serializers.CharField(max_length=100)
    class Meta:
        model = get_user_model()
        fields=('id','user')
    def to_representation(self, instance):
        data=super().to_representation(instance)
        return data

class postSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = post
        fields = ('id','user', 'caption','photo','date_created','date_updated')
    
    # def create(self, validated_data):
    #     profile_data = validated_data.pop('user')
    #     user = User.objects.create(**validated_data)
    #     user.objects.create(user=user, **profile_data)
    #     return user 
    # def create(self, validated_data):
    #     return post(**validated_data)
    # def create(self, validated_data):
    #     order = User.objects.get(pk=validated_data.pop('user'))
    #     instance = post.objects.create(**validated_data)
    #     Assignment.objects.create(User=order, post=instance)
    #     return instance


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    photo= postSerializer(read_only=True)
    class Meta:
        model = Like
        fields = ('id','user', 'photo','date_created')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    photo= postSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id','user', 'photo','date_created','content')
