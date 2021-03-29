# Generated by Django 3.1.7 on 2021-03-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='Слайдер')),
                ('active', models.CharField(blank=True, help_text="Только для первого слайда написать 'active', к остальным не писать, возможно возникнет ошибка", max_length=6, null=True)),
            ],
            options={
                'verbose_name_plural': 'Слайдер',
            },
        ),
    ]