# Generated by Django 4.1 on 2022-09-11 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nuguhome", "0010_alter_score_score"),
    ]

    operations = [
        migrations.AlterField(
            model_name="score",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
