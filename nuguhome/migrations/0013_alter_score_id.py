# Generated by Django 4.1 on 2022-09-11 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("nuguhome", "0012_alter_score_score"),
    ]

    operations = [
        migrations.AlterField(
            model_name="score",
            name="id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="nuguhome.trainer",
            ),
        ),
    ]
