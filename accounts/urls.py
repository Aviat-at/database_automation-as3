from django.urls import path
from .views import login_view, success_view, register_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('success/', success_view, name='success'),
]
