from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class Testimonial(models.Model):
    title = models.CharField(verbose_name="Имя Фамилие", max_length=250)
    sub_title = models.CharField(
        verbose_name="Курс", max_length=200, blank=True, null=True, 
        help_text="Пример: Окончил курс по Программированию, Робототехнике и т.д."
    )
    testimonial = RichTextUploadingField(verbose_name="Отзыв человека", blank=True, null=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name_plural = "Отзывы"