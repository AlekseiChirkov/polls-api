# Generated by Django 2.2.10 on 2021-07-05 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('description', models.TextField(blank=True, max_length=512, null=True)),
                ('start_date', models.DateField(auto_now_add=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Poll',
                'verbose_name_plural': 'Polls',
            },
        ),
        migrations.CreateModel(
            name='PollChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(blank=True, max_length=512, null=True)),
                ('question_type', models.CharField(blank=True, choices=[('Text answer', 'Text answer'), ('Single answer', 'Single answer'), ('Multiple answers', 'Multiple answers')], max_length=64, null=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
            ],
            options={
                'verbose_name': 'Poll Question',
                'verbose_name_plural': 'Poll Questions',
            },
        ),
    ]
