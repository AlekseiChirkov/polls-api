from django.urls import path

from apps.authentication.views import UserCreateAPIView


urlpatterns = [
    path('register/', UserCreateAPIView.as_view()),
]
