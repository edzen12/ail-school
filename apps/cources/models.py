from django.db import models


class CategoryCourses(models.Model):
    title = models.CharField(verbose_name="Категория", max_length=100)
    icon = models.ImageField(verbose_name="Иконка категории", upload_to="courses/", blank=True, null=True)
    image = models.ImageField(verbose_name="Фото категории", upload_to="courses/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Категории"

class Courses(models.Model):
    category = models.ForeignKey(CategoryCourses, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Название", max_length=100)
    sub_title = models.CharField(verbose_name="Под заголовок", max_length=100, blank=True, null=True)
    image = models.ImageField(verbose_name="Фото", upload_to="courses/", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Курсы"