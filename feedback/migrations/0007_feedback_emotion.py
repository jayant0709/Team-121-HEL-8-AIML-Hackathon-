# Generated by Django 4.1.13 on 2024-07-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_remove_feedback_question_10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='emotion',
            field=models.CharField(default='Not analyzed', max_length=50),
        ),
    ]
