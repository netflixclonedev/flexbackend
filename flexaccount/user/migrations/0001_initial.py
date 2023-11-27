# Generated by Django 4.2.7 on 2023-11-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Userdata",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("username", models.CharField(max_length=200)),
                ("password", models.CharField(max_length=16)),
            ],
        ),
    ]