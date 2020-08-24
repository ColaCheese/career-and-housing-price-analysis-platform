from scrapy import cmdline

cmdline.execute("scrapy crawl rent -o result.json".split())