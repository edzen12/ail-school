# Generated by Django 3.1.7 on 2021-03-17 08:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club_and', '0002_club_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]