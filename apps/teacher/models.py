from django.db import models
from django.urls import reverse


class Teacher(models.Model):
    name = models.CharField(verbose_name="Имя Фамилие", max_length=100)
    sub_title = models.CharField(
        verbose_name="Предмет", max_length=50, blank=True, null=True, 
        help_text="Пример: Учитель по программированию, Робототехнике, Английскому и т.д."
    )
    image = models.ImageField(verbose_name="Фото", blank=True, null=True, upload_to="teacher/")
    descrip = models.TextField(verbose_name="Описание того кто он(а) и что закончил(а)", blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("teacher_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = "Преподы"