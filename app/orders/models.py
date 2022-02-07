from django.db import models


class Order(models.Model):
    subject = models.CharField("Предмет", max_length=255)
    description = models.TextField("Описание")
    created_at = models.DateTimeField("Дата и время создания", auto_now_add=True)
    expected_finished_at = models.DateTimeField("Ожидаемое время завершения", null=True)
    finished_at = models.DateTimeField("Время завершения", null=True)
    is_finished = models.BooleanField("Завершен", default=False)
    assignee = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="orders",
                                 verbose_name="Ответственный", null=True, blank=True)
    client = models.ForeignKey("clients.Client", on_delete=models.PROTECT, related_name="orders", verbose_name="Клиент")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"{self.subject} - #{self.id}"
