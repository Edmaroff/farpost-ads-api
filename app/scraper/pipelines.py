from asgiref.sync import sync_to_async
from backend.models import Advertisement


class AdvertisementPipeline:
    """
    Пайплайн для обработки и сохранения объявлений в базу данных
    """

    def open_spider(self, spider):
        """
        Очищает таблицу Advertisement при открытии паука
        """

        Advertisement.objects.all().delete()

    async def process_item(self, item, spider):
        """
        Асинхронно обрабатывает каждый элемент, собранный пауком.
        """

        await sync_to_async(self.create_advertisement)(item)
        return item

    def create_advertisement(self, item):
        """
        Создает новую запись Advertisement в БД
        """
        Advertisement.objects.create(
            title=item["title"],
            farpost_id=item["farpost_id"],
            views_count=item["views_count"],
            position=item["position"],
            author=item["author"],
        )
