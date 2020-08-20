from scrapy import cmdline

print('start')
cmdline.execute("scrapy crawl soldHouse -o resultNewData.json".split())

