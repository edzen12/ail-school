from django.db import models


class Testimonial(models.Model):
    title = models.CharField(verbose_name="Имя Фамилие", max_length=100)
    sub_title = models.CharField(
        verbose_name="Курс", max_length=80, blank=True, null=True, 
        help_text="Пример: Окончил курс по Программированию, Робототехнике и т.д."
    )
    image = models.ImageField(verbose_name="Фото", blank=True, null=True, upload_to="testimonial/")
    testimonial = models.TextField(verbose_name="Отзыв человека", blank=True, null=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name_plural = "Отзывы"