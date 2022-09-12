# Generated by Django 4.1 on 2022-09-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="gymlocation",
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
                ("gym", models.TextField(default="")),
                ("location", models.TextField(default="")),
            ],
        ),
        migrations.CreateModel(
            name="trainer",
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
                ("gym", models.CharField(default="", max_length=20)),
                ("name", models.CharField(default="", max_length=10)),
                ("like", models.IntegerField(default=0)),
                ("dislike", models.IntegerField(default=0)),
                ("mapurl", models.TextField(default="")),
                ("inform", models.TextField(default="")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
