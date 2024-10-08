# Generated by Django 5.1 on 2024-08-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="upload_test_information",
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
                ("test_category", models.CharField(max_length=255)),
                ("test_name", models.CharField(max_length=255)),
                ("test_fees", models.FloatField()),
                ("test_id", models.CharField(max_length=255)),
                ("patient_id", models.CharField(max_length=255)),
            ],
        ),
    ]
