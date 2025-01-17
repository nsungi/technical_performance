# Generated by Django 4.2.10 on 2024-04-10 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_feedback_technician_alter_feedback_message"),
    ]

    operations = [
        migrations.CreateModel(
            name="Conversation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("last_message_content", models.TextField(blank=True)),
                ("last_message_timestamp", models.DateTimeField(null=True)),
                (
                    "last_message_sender",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="last_message_sender",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="conversations_as_user1",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="conversations_as_user2",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="feedback",
            name="message",
            field=models.CharField(
                choices=[("accepted", "Accepted"), ("rejected", "Rejected")],
                default="accepted",
                max_length=10,
            ),
        ),
        migrations.DeleteModel(
            name="Collaboration",
        ),
    ]
