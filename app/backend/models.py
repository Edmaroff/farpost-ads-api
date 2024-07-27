from django.db import models


class Advertisement(models.Model):
    """
    Модель для хранения данных об объявлениях
    Attributes:
        title (str): Заголовок объявления
        farpost_id (int): ID объявления на сайте Farpost
        author (str): Автор объявления
        views_count (int): Количество просмотров объявления
        position (int): Позиция объявления в списке
    """

    title = models.CharField(max_length=255, verbose_name="Название")
    farpost_id = models.IntegerField(verbose_name="ID в Farpost")
    author = models.CharField(max_length=120, verbose_name="Автор")
    views_count = models.IntegerField(verbose_name="Количество просмотров")
    position = models.IntegerField(verbose_name="Позиция")

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["position"]

    def __str__(self):
        return f"{self.title} ({self.author})"
