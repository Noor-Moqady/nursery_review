# Generated by Django 2.2.4 on 2023-12-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_nursery_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nursery',
            name='contact_number',
            field=models.CharField(max_length=225),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]