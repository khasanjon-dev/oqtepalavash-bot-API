from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import User
from users.serializers.user import UserModelSerializer, RegisterSerializer


class UserViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    @action(methods=['post'], detail=False, serializer_class=RegisterSerializer, url_path='user')
    def get_or_create_user(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        telegram_id = serializer.data.get('telegram_id')
        user, created = User.objects.get_or_create(telegram_id=telegram_id)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)
