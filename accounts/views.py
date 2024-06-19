from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from accounts.serializers import UserSerializer
from rest_framework.generics import CreateAPIView


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            return redirect(reverse('login'))
        return response
 
    
class CustomLoginView(LoginView):

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.is_authenticated:
            return redirect(reverse('upload'))
        return response