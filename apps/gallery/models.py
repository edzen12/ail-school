from django.db import models


class Gallery(models.Model):
    image = models.ImageField(verbose_name="Галерея", upload_to="gallery/")

    class Meta:
        verbose_name_plural = "Галерея"


class Slider(models.Model):
    image = models.ImageField(verbose_name="Слайдер", upload_to="gallery/")
    active = models.CharField(
        max_length=6, 
        blank=True, null=True,
        help_text="Только для первого слайда написать 'active', к остальным не писать, возможно возникнет ошибка"
    )

    class Meta:
        verbose_name_plural = "Слайдер"