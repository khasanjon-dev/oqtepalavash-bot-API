from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('telegram_id', 'phone', 'city', 'language')


class RegisterSerializer(Serializer):
    telegram_id = serializers.IntegerField()

    def validate(self, attrs):
        telegram_id = attrs.get('telegram_id')
        if User.objects.filter(telegram_id=telegram_id).exists():
            raise ValidationError('Bunday user mavjud!')
        return attrs
