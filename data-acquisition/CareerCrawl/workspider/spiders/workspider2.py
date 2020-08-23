import scrapy
import time

from ..items import Workspider2Item


class WorkSpider(scrapy.Spider):
    city = ['北京', '上海', '广州', '成都', '武汉',
            '南京', '杭州', '合肥', '南昌', '福州', '济南', '宁波', '青岛', '无锡', '厦门', '烟台', '金华', '温州', '泉州',
            '长沙', '郑州', '天津', '石家庄', '呼和浩特', '太原',
            '西安', '兰州', '银川',
            '海口', '惠州', '珠海', '佛山', '东莞',
            '昆明', '重庆', '贵阳',
            '哈尔滨', '长春', '沈阳', '大连']
    dir = ['开发', '算法', '测试', '前端']
    cnt = [0, 0, 0, 0]
    i = 0

    # 爬虫名字
    name = 'work2'
    # 设置访问域
    allowed_domains = ['jobui.com']
    # 开始连接 北京 开发
    start_urls = ['https://www.jobui.com/jobs?jobKw={}&cityKw={}&industry=计算机软件'.format(dir[i], city[cnt[i]])]

    # sleep_time = random.randint(1, 5) + random.random()
 

    def parse(self, response):
        # 创建items实例
        item = Workspider2Item()

        # wait 500ms
        time.sleep(0.5)

        item['number'] = response.xpath('//li[@class="fr"]/span[@class="sort-cut-result"]/span/text()').extract()[0]

        item['location'] = self.city[self.cnt[self.i]]

        item['direction'] = self.dir[self.i]

        yield item

        # 换城市
        if (self.cnt[self.i] < 39) & (self.i < 4):
            self.cnt[self.i] = self.cnt[self.i] + 1
            print(self.i)
            print(self.cnt)
            if (self.cnt[self.i] < 40):
                yield scrapy.Request(
                    'https://www.jobui.com/jobs?jobKw={}&cityKw={}&industry=计算机软件'.format(self.dir[self.i],
                                                                                          self.city[self.cnt[self.i]]),
                    callback=self.parse)
        # 换方向
        elif self.i < 3:
            self.i = self.i + 1
            yield scrapy.Request(
                'https://www.jobui.com/jobs?jobKw={}&cityKw={}&industry=计算机软件'.format(self.dir[self.i],
                                                                                      self.city[self.cnt[self.i]]),
                callback=self.parse)
        else:
            print('finish')
