# Generated by Django 4.2.10 on 2024-04-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_category_contactinfo_alter_service_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(upload_to="avatars/"),
        ),
    ]
