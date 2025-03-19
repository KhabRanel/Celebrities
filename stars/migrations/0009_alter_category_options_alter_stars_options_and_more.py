# Generated by Django 5.1.6 on 2025-03-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0008_alter_stars_options_stars_time_create_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='stars',
            options={'ordering': ['-time_create'], 'verbose_name': 'Знаменитости', 'verbose_name_plural': 'Знаменитости'},
        ),
        migrations.AddField(
            model_name='stars',
            name='full_content',
            field=models.TextField(blank=True, verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='stars',
            name='birth_date',
            field=models.DateField(blank=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='stars',
            name='content',
            field=models.TextField(blank=True, verbose_name='Краткая биография'),
        ),
        migrations.AlterField(
            model_name='stars',
            name='country',
            field=models.TextField(blank=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='stars',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Draft'), (True, 'Published')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='stars',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='stars',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='stars',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
        migrations.AddIndex(
            model_name='stars',
            index=models.Index(fields=['-time_create'], name='stars_stars_time_cr_e8721e_idx'),
        ),
    ]
