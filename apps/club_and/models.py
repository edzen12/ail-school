from django.db import models


class Club(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=150)
    image = models.ImageField(verbose_name="Фото", upload_to="club/", blank=True, null=True)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Кружки и Клубы"
    