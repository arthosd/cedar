from scrapy.crawler import CrawlerProcess


def start_process(processes, settings={"FEEDS": {"result.json": {"format": "json"}}}):

    process = CrawlerProcess(settings=settings)

    for proc in processes:
        process.crawl(proc)

    process.start()
