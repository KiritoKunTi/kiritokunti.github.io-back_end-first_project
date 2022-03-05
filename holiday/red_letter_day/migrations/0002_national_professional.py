# Generated by Django 4.0.2 on 2022-03-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red_letter_day', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='National',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Мейрам атауы')),
                ('on_date', models.CharField(max_length=20, verbose_name='Күн-айы')),
                ('anons', models.TextField(verbose_name='Мейрам жайлы')),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Мейрам атауы')),
                ('on_date', models.CharField(max_length=20, verbose_name='Күн-айы')),
                ('anons', models.TextField(verbose_name='Мейрам жайлы')),
            ],
        ),
    ]