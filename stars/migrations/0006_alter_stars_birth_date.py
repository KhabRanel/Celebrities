# Generated by Django 5.1.6 on 2025-02-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0005_alter_stars_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stars',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
    ]
