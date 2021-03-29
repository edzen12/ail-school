from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Vacancie(models.Model):
    title = models.CharField(verbose_name="Заголовок", blank=True, null=True, max_length=150)
    desc = RichTextUploadingField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(upload_to="vacancie/", verbose_name="Фото", blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("vacancie_detail", kwargs={"slug": self.slug})
        
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Вакансии"
    
