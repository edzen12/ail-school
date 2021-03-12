from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100)
    sub_title = models.CharField(
        verbose_name="Под заголовок", max_length=30, blank=True, null=True, 
        help_text="Пример: Образование, Курсы, Технологии и т.д."
    )
    image = models.ImageField(verbose_name="Фото", blank=True, null=True, upload_to="news/")
    descrip = models.TextField(verbose_name="Описание", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Новости"