# Generated by Django 3.1.7 on 2021-04-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210317_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='sub_title',
            field=models.CharField(blank=True, help_text='Пример: Образование, Курсы, Технологии и т.д.', max_length=200, null=True, verbose_name='Под заголовок'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]