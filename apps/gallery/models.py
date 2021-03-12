from django.db import models


class Gallery(models.Model):
    image = models.ImageField(verbose_name="Галерея", upload_to="gallery/")

    class Meta:
        verbose_name_plural = "Галерея"
