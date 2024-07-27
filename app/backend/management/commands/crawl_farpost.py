from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraper.spiders.farpost import FarpostSpider


class Command(BaseCommand):
    help = "Запуск паука FarpostSpider"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(FarpostSpider)
        process.start()
        self.stdout.write(self.style.SUCCESS("Паук завершил работу"))
