from datetime import date

from django.db.models import Q
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.polls.models import Poll, UserAnswer
from apps.polls.serializers import (
    PollSerializer, UserAnswerSerializer, UserAnswerDetailSerializer
)
from apps.polls.services import get_client_ip


class PollListAPIView(ListAPIView):
    serializer_class = PollSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        poll_qs = Poll.objects.filter(end_date__gt=date.today())
        return poll_qs


class UserAnswerCreateAPIVIew(CreateAPIView):
    serializer_class = UserAnswerSerializer
    permission_classes = (AllowAny, )
    queryset = UserAnswer


class UserAnswerListAPIView(ListAPIView):
    serializer_class = UserAnswerDetailSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user_id = self.request.user.id
        answer = UserAnswer.objects.filter(
            Q(anonymous_user_id=user_id) | Q(user_id=user_id)
        )
        return answer
