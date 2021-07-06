from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from apps.authentication.serializers import CreateUserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
