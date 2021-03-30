# Generated by Django 3.1.7 on 2021-03-29 15:32

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_big_title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Заголовок 1й карточки')),
                ('one_big_desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание 1й карточки')),
                ('one_big_image', models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Фото 1й карточки')),
                ('one_medium_image', models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Фото 1й карточки')),
                ('two_big_title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Заголовок 2й карточки')),
                ('two_big_desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание 2й карточки')),
                ('two_big_image', models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Фото 2й карточки')),
                ('three_big_title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Наша миссия')),
                ('three_big_desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание миссии')),
                ('four_big_title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Наша философия')),
                ('four_big_desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание философии')),
                ('five_big_title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Заголовок 5й карточки')),
                ('five_big_desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание 5й карточки')),
                ('five_big_image', models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Фото 5й карточки')),
                ('six_big_title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Заголовок 6й карточки')),
                ('six_big_desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание 6й карточки')),
                ('six_big_image', models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Фото 6й карточки')),
            ],
            options={
                'verbose_name_plural': 'О НАС',
                'ordering': ['-id'],
            },
        ),
    ]
