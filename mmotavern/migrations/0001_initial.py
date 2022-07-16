# Generated by Django 3.2.6 on 2021-12-07 00:33

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('time_of_creation', models.TimeField(auto_now_add=True)),
                ('datetime_of_creation', models.DateTimeField(auto_now_add=True)),
                ('date_of_last_update', models.DateField(auto_now=True)),
                ('time_of_last_update', models.TimeField(auto_now=True)),
                ('datetime_of_last_update', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmotavern.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1500)),
                ('confirmed', models.BooleanField(blank=True, null=True, verbose_name='Подтвержден')),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('time_of_creation', models.TimeField(auto_now_add=True)),
                ('datetime_of_creation', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmotavern.post')),
            ],
        ),
    ]
