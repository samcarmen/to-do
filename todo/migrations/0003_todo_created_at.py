# Generated by Django 4.2.4 on 2023-09-03 07:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_user_last_login_time_user_status_todo"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
