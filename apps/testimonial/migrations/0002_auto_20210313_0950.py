# Generated by Django 3.1.7 on 2021-03-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='sub_title',
            field=models.CharField(blank=True, help_text='Пример: Окончил курс по Программированию, Робототехнике и т.д.', max_length=80, null=True, verbose_name='Курс'),
        ),
    ]
