# Generated by Django 2.2.4 on 2023-12-20 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20231220_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='programs',
            name='childage_max',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='programs',
            name='childage_min',
            field=models.IntegerField(null=True),
        ),
    ]
