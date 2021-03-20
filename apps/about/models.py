from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class AboutUs(models.Model):
    one_big_title = models.CharField(
        verbose_name="Заголовок 1й карточки", max_length=150, blank=True, null=True)
    one_big_desc = RichTextUploadingField(
        verbose_name="Описание 1й карточки", blank=True, null=True)
    one_big_image = models.ImageField(
        verbose_name="Фото 1й карточки", upload_to="about/", blank=True, null=True)
    one_medium_image = models.ImageField(
        verbose_name="Фото 1й карточки", upload_to="about/", blank=True, null=True)

    two_big_title = models.CharField(
        verbose_name="Заголовок 2й карточки", max_length=150, blank=True, null=True)
    two_big_desc = RichTextUploadingField(
        verbose_name="Описание 2й карточки", blank=True, null=True)
    two_big_image = models.ImageField(
        verbose_name="Фото 2й карточки", upload_to="about/", blank=True, null=True)

    three_big_title = models.CharField(
        verbose_name="Наша миссия", max_length=150, blank=True, null=True)
    three_big_desc = RichTextUploadingField(
        verbose_name="Описание миссии", blank=True, null=True)

    four_big_title = models.CharField(
        verbose_name="Наша философия", max_length=150, blank=True, null=True)
    four_big_desc = RichTextUploadingField(
        verbose_name="Описание философии", blank=True, null=True)

    five_big_title = models.CharField(
        verbose_name="Заголовок 5й карточки", max_length=150, blank=True, null=True)
    five_big_desc = RichTextUploadingField(
        verbose_name="Описание 5й карточки", blank=True, null=True)
    five_big_image = models.ImageField(
        upload_to="about/", verbose_name="Фото 5й карточки", blank=True, null=True)

    six_big_title = models.CharField(
        verbose_name="Заголовок 6й карточки", max_length=150, blank=True, null=True)
    six_big_desc = RichTextUploadingField(
        verbose_name="Описание 6й карточки", blank=True, null=True)
    six_big_image = models.ImageField(
        upload_to="about/", verbose_name="Фото 6й карточки", blank=True, null=True)


    def __str__(self):
        return self.one_big_title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "О НАС"
