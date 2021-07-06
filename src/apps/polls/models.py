from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    """
    Polls model to create by admin and to pass by users
    """

    title = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(max_length=512, blank=True, null=True)
    start_date = models.DateField(auto_now_add=True, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'

    def __str__(self):
        return self.title


class PollChoice(models.Model):
    """
    Polls questions model to add questions to polls
    """

    CHOICE_TYPES = (
        ("Text answer", "Text answer"),
        ("Single answer", "Single answer"),
        ("Multiple answers", "Multiple answers"),
    )

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=512, blank=True, null=True)
    choice_type = models.CharField(
        max_length=64, choices=CHOICE_TYPES, blank=True, null=True
    )

    class Meta:
        verbose_name = "Poll Choice"
        verbose_name_plural = "Poll Choices"

    def __str__(self):
        return self.choice_text


class UserAnswer(models.Model):
    anonymous_user_id = models.IntegerField(
        verbose_name='Anonymous user id', blank=True, null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    poll_choice = models.ForeignKey(PollChoice, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "User's poll choice"
        verbose_name_plural = "User's poll choices"

    def __str__(self):
        return f'{self.poll} - {self.user_id}'



