import scrapy
from ..items import RentItem  # 引入items/DouBanSpiderItem类


class RentSpider(scrapy.Spider):
    # 爬取城市
    # 北京市：北京；天津；上海；重庆 ；石家庄 ；太原 ；西安 ；济南；郑州 ；沈阳 ；
    # 长春 ；哈尔滨 ；南京 ；杭州 ；合肥 ；南昌； 福州； 武汉；长沙；  成都；  贵阳；
    # 昆明；  广州；  海口；  兰州； 西宁；  台北；呼和浩特；  乌鲁木齐；  拉萨；
    # 南宁；银川；香港；澳门。
    citys = [("北京", "bj"), ("天津", "tj"), ("上海", "sh"), ("重庆", "cq"), ("石家庄", "sjz"), ("太原", "ty"),
             ("西安", "xa"), ("济南", "jn"), ("郑州", "zj"), ("沈阳",
                                                        "sy"), ("长春", "cc"), ("哈尔滨", "hrb"),
             ("南京", "nj"), ("杭州", "hz"), ("合肥", "hf"), ("南昌",
                                                        "nc"), ("福州", "fz"), ("武汉", "wh"),
             ("长沙", "cs"), ("成都", "cd"), ("贵阳", "gy"), ("昆明",
                                                        "km"), ("广州", "gz"), ("海口", "hk"),
             ("兰州", "lz"), ("呼和浩特", "hhht"), ("银川",
                                              "yc"), ("宁波", "nb"), ("大连", "dl"), ("青岛", "qd"),
             ("无锡", "wx"), ("厦门", "xm"), ("烟台", "yt"), ("金华",
                                                        "jh"), ("温州", "wz"), ("泉州", "quanzhou"),
             ("惠州", "hui"), ("珠海", "zh"), ("佛山", "fs"), ("东莞", "dg")]
    # citys = [("珠海", "zh")]
    # 租房缺少：香港、澳门、乌鲁木齐、南宁、拉萨、西宁、台北地区信息
    cnt = 0
    max = len(citys)
    # 爬虫名字 启动调用
    name = "rent"
    # 定义访问域
    allowed_domains = ['ke.com']
    # 开始连接
    start_urls = ['https://{}.zu.ke.com/zufang/'.format(citys[cnt][1])]

    # 实现spider.parse函数

    def parse(self, response):

        # 创建实例 item用于保存字典
        item = RentItem()
        # print(response.body)
        # 打印
        all = response.xpath('//div[@class="content__list--item--main"]')
        number = response.xpath(
            '//span[@class="content__title--hl"]/text()').extract()[0]
        for each in all:

            price = each.xpath(
                'span[@class="content__list--item-price"]/em/text()')

            location = each.xpath(
                'p[@class="content__list--item--des"]/a/text()')


            if price and len(price.extract()[0]) < 7:
                item['price'] = price.extract()[0]

            if location and len(location.extract()[0]) > 0:
                item['location'] = location.extract()[0]
                # print(type(location.extract()[0]))
                item['city'] = self.citys[self.cnt][0]
                item['number'] = number

            # yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。
            # 重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。
            # return 的作用：如果没有 return，则默认执行至函数完毕，返回的值一般是yield的变量
            # yield= return+记住返回位置           
            yield item
        nextlink = response.xpath(
            '//div[@class="content__pg"]//@data-curpage').extract()
        total = int(response.xpath(
            '//div[@class="content__pg"]//@data-totalpage').extract()[0])
        next = int(nextlink[0]) + 1
        #  print(current)
        # print(total)
        if next <= total and next <= 100:
            # 翻页
            yield scrapy.Request('https://%s.zu.ke.com/zufang/pg%s/#contentList' % (
                self.citys[self.cnt][1], next),
                callback=self.parse)
        else:
            self.cnt += 1
            if self.cnt <= self.max:
                yield scrapy.Request('https://%s.zu.ke.com/zufang/pg1/#contentList' % (self.citys[self.cnt][1]), callback=self.parse)
            else:
                print("finish")
