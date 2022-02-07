from django.db import models


class Client(models.Model):
    full_name = models.CharField("Имя", max_length=255)
    phone = models.CharField("Телефон", max_length=15, blank=True)
    email = models.EmailField("Почта", blank=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.full_name
