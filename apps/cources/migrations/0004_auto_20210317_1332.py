# Generated by Django 3.1.7 on 2021-03-17 13:32

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cources', '0003_auto_20210317_0812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorycourses',
            options={'verbose_name_plural': 'Курсы'},
        ),
        migrations.AddField(
            model_name='categorycourses',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='categorycourses',
            name='sub_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Под заголовок'),
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
    ]
