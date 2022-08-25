# Generated by Django 4.1 on 2022-08-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=264, unique=True)),
                ("surname", models.CharField(max_length=264, unique=True)),
                ("mail", models.EmailField(max_length=264)),
            ],
        ),
    ]
