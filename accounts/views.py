from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

