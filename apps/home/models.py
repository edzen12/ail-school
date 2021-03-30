from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Setting(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название сайта", null=True)
    logo = models.ImageField(verbose_name="Логотип сайта", upload_to="logo/", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="Описание сайта", blank=True, null=True)

    address = models.CharField(verbose_name="Адрес", max_length=255, blank=True, null=True)
    phone_1 = models.CharField(verbose_name="Номер 1го телефона", max_length=13, blank=True, null=True)
    phone_2 = models.CharField(verbose_name="Номер 2го телефона", blank=True,max_length=13, null=True)
    email = models.CharField(verbose_name="E-mail", blank=True,max_length=155, null=True)
    time_work = models.CharField(verbose_name="Время работы", blank=True,max_length=255, null=True)

    banner_title = models.CharField(max_length=150, verbose_name="Баннер большой заголовок", blank=True, null=True)
    banner_big_title = models.CharField(max_length=150, verbose_name="Баннер мини заголовок", blank=True, null=True)
    banner_desc = models.TextField(verbose_name="Баннер большой Описание", blank=True, null=True)


    instagram = models.CharField(blank=True,max_length=255, verbose_name="Ссылка на Instagram", null=True)
    whatsapp = models.CharField(blank=True, max_length=13, verbose_name="WhatsApp номер", null=True)
    facebook = models.CharField(blank=True,max_length=255, verbose_name="Ссылка на Facebook", null=True)
    
    usloviya = RichTextUploadingField(verbose_name="Условия приема", blank=True, null=True)

    politic_polojeniya = RichTextUploadingField(verbose_name="Политика и Положения", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Основные настройки"