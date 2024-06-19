from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import status
from accounts.serializers import RegisterSerializer, LoginSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            login_url = request.build_absolute_uri(reverse('login'))
            print(f"Registration successful, redirecting to: {login_url}")
            return redirect(login_url)
        else:
            print(f"Registration failed with status code: {response.status_code}")
        return response
 
    
class LoginView(APIView):

    def get(self, request):
        return Response({'message': 'Login page'})

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                upload_url = reverse('upload')
                return redirect(upload_url)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)