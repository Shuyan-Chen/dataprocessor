from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer
from django.shortcuts import redirect
from django.urls import reverse

class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            return redirect(reverse('upload'))
        return response