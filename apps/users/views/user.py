from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import User
from users.serializers import UserSerializer
from users.serializers.user import UserModelSerializer


class UserViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    @action(methods=['post'], detail=False, serializer_class=UserSerializer, url_path='user')
    def get_or_create_user(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        telegram_id = serializer.data.get('telegram_id')
        if User.objects.filter(telegram_id=telegram_id).exists():
            serializer.data.pop('telegram_id')
            User.objects.filter(telegram_id=telegram_id).update(**serializer.data)
            return Response(serializer.data)
        User.objects.create(**serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED)
    # @action(methods=['get'], detail=False, serializer_class=)
