from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('telegram_id', 'phone', 'city', 'language')


class RegisterSerializer(Serializer):
    telegram_id = serializers.IntegerField()

