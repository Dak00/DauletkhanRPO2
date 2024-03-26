from django.db import models

class Food(models.Model):
    name = models.CharField("Название блюда", max_length=100)
    description = models.CharField("Описание", max_length=100)
    image = models.URLField("Ссылка на фото", max_length=500)
    price = models.IntegerField("Цена")

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def __str__(self):
        return self.name
