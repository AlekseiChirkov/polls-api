from django.urls import path

from apps.polls.views import (
    PollListAPIView, UserAnswerCreateAPIVIew, UserAnswerListAPIView
)

urlpatterns = [
    path('list/', PollListAPIView.as_view()),
    path('create/', UserAnswerCreateAPIVIew.as_view()),
    path('answers/', UserAnswerListAPIView.as_view()),
]
