# Generated by Django 4.2.10 on 2024-04-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0013_projectdocument_contract_appointment_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contract",
            name="technician_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="contract",
            name="title",
            field=models.CharField(
                choices=[
                    ("IT Support", "IT Support contract"),
                    ("Network Maintenance", "Network Maintenance contract"),
                    ("Electrical Maintenance", "Electrical Maintenance contract"),
                    ("Plumbing Maintenance", "Plumbing Maintenance contract"),
                ],
                max_length=100,
            ),
        ),
    ]
