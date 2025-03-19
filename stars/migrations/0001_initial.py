# Generated by Django 5.1.6 on 2025-02-06 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.TextField(blank=True)),
                ('category', models.TextField(blank=True)),
                ('birth_date', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
