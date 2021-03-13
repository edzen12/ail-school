from django.db import models


class Advantage(models.Model):
    image = models.ImageField(verbose_name="Иконка", blank=True, null=True, upload_to="news/", help_text="должно быть качества .PNG")
    descrip = models.TextField(verbose_name="Описание", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.descrip}"

    class Meta:
        verbose_name_plural = "Преимущества"
