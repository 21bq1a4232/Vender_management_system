# Generated by Django 4.2.5 on 2023-12-14 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="vendor_code",
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]