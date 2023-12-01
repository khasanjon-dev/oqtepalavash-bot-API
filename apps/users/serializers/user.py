from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer

from users.models import User


class UserSerializer(Serializer):
    telegram_id = serializers.IntegerField(required=False)
    phone = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    language = serializers.CharField(required=False)


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('telegram_id', 'phone', 'city', 'language')
