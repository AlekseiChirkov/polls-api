from rest_framework import serializers

from apps.polls.models import Poll, PollChoice, UserAnswer
from apps.authentication.serializers import UserSerializer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"


class PollChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollChoice
        fields = "__all__"


class UserAnswerSerializer(serializers.ModelSerializer):
    anonymous = serializers.BooleanField(write_only=True)

    class Meta:
        model = UserAnswer
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get("request")
        anonymous = validated_data['anonymous']
        if anonymous:
            answer = UserAnswer.objects.create(
                anonymous_user_id=int(request.user.id),
                poll=validated_data['poll'],
                poll_choice=validated_data['poll_choice']
            )
            return answer

        answer = UserAnswer.objects.create(
            user_id=request.user.id,
            poll=validated_data['poll'],
            poll_choice=validated_data['poll_choice']
        )
        return answer


class UserAnswerDetailSerializer(serializers.ModelSerializer):
    poll = PollSerializer()
    poll_choice = PollChoiceSerializer()

    class Meta:
        model = UserAnswer
        fields = "__all__"
