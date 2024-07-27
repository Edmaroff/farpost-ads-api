import scrapy


class AdvertisementItem(scrapy.Item):
    """
    Определяет структуру данных для объявления, собираемого пауком
    """

    title = scrapy.Field()
    farpost_id = scrapy.Field()
    views_count = scrapy.Field()
    position = scrapy.Field()
    author = scrapy.Field()
