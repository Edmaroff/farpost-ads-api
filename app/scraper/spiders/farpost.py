import scrapy
from scrapy.http import Request
import random
from faker import Faker

from app.settings import MAX_COUNT_ADS
from scraper.items import AdvertisementItem


class FarpostSpider(scrapy.Spider):
    """
    Паук для сбора данных с сайта Farpost
    """

    name = "farpost"
    allowed_domains = ["farpost.ru"]
    start_urls = [
        "https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"
    ]

    def parse(self, response, **kwargs):
        """
        Парсит страницу со списком объявлений и отправляет запросы на страницы отдельных объявлений
        """

        ads = response.css("tr.bull-list-item-js.-exact")[:MAX_COUNT_ADS]

        if not ads:
            # В случае блокировок, генерируем случайные данные для БД
            self.log("Нет объявлений - генерируем тестовые данные")
            fake = Faker("ru_RU")

            for i in range(MAX_COUNT_ADS):
                item = AdvertisementItem(
                    title=fake.catch_phrase(),
                    farpost_id=random.randint(1000000, 9999999),
                    views_count=random.randint(10, 5000),
                    position=i + 1,
                    author=fake.name(),
                )
                yield item

        for position, ad in enumerate(ads, 1):
            title = (
                ad.css("a.bulletinLink.bull-item__self-link.auto-shy::text")
                .get()
                .strip()
            )
            farpost_id = int(ad.attrib["data-doc-id"])
            views_count = int(ad.css("span.views.nano-eye-text::text").get().strip())

            url_ad = ad.css("a.bulletinLink.bull-item__self-link.auto-shy").attrib[
                "href"
            ]
            full_url = response.urljoin(url_ad)
            request = Request(full_url, callback=self.parse_ad)
            request.meta.update(
                {
                    "title": title,
                    "farpost_id": farpost_id,
                    "views_count": views_count,
                    "position": position,
                }
            )
            yield request

    def parse_ad(self, response):
        """
        Парсит страницу отдельного объявления и создает элемент AdvertisementItem
        """

        author = response.css("span.userNick.auto-shy a::text").get().strip()
        item = AdvertisementItem(
            title=response.meta["title"],
            farpost_id=response.meta["farpost_id"],
            views_count=response.meta["views_count"],
            position=response.meta["position"],
            author=author,
        )
        yield item
