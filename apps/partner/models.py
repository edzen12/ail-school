from django.db import models


class Partners(models.Model):
    title = models.CharField(verbose_name="Название", blank=True, null=True, max_length=50)
    image = models.ImageField(verbose_name="Лого", blank=True, null=True, upload_to="partners/")

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name_plural = "Партнёры"