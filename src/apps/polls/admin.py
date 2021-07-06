from django.contrib import admin

from apps.polls.models import Poll, PollChoice


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Poll._meta.fields]

    class Meta:
        model = Poll


@admin.register(PollChoice)
class PollChoiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PollChoice._meta.fields]

    class Meta:
        model = PollChoice
