# Generated by Django 5.1 on 2024-08-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0003_test_request_details"),
    ]

    operations = [
        migrations.CreateModel(
            name="upload_result",
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
                ("test_id", models.CharField(max_length=10)),
                ("patient_id", models.CharField(max_length=10)),
                ("result_upload_date", models.DateTimeField(auto_now_add=True)),
                ("doctor_name", models.CharField(max_length=20)),
                ("doctor_fees", models.IntegerField()),
                ("day_visited", models.DateTimeField()),
                ("test_fees", models.IntegerField()),
                ("hospital_location", models.CharField(max_length=30)),
                ("token_number", models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name="test_request_details",
            name="country",
            field=models.CharField(default="India", max_length=255),
        ),
        migrations.AddField(
            model_name="test_request_details",
            name="email_id",
            field=models.EmailField(default="arun@gmail.com", max_length=254),
        ),
        migrations.AddField(
            model_name="test_request_details",
            name="phone_number",
            field=models.IntegerField(default=999999999999),
        ),
        migrations.AddField(
            model_name="test_request_details",
            name="pincode",
            field=models.IntegerField(default=678678),
        ),
        migrations.AddField(
            model_name="test_request_details",
            name="state",
            field=models.CharField(default="Tamilnadu", max_length=255),
        ),
        migrations.AlterField(
            model_name="test_request_details",
            name="date_of_birth",
            field=models.DateField(),
        ),
    ]
