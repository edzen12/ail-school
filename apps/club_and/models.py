from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField



class Club(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=150)
    image = models.ImageField(verbose_name="Фото", upload_to="club/", blank=True, null=True)
    desc = RichTextUploadingField(verbose_name="Описание", blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("club_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Кружки и Клубы"
    