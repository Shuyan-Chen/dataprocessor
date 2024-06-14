from django.urls import path
from .views import RegisterAPIView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', login_required(auth_views.LoginView.as_view()), name='login'),
    path('logout/', login_required(auth_views.LogoutView.as_view()), name='logout'),
]