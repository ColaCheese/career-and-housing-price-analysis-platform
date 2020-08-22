import math
import scrapy
import time
import random
from ..items import WorkspiderItem


class WorkSpider(scrapy.Spider):
    city = ['北京', '上海', '广州', '成都', '武汉',
            '南京', '杭州', '合肥', '南昌', '福州', '济南', '宁波', '青岛', '无锡', '厦门', '烟台', '金华', '温州', '泉州',
            '长沙', '郑州', '天津', '石家庄', '呼和浩特', '太原',
            '西安', '兰州', '银川',
            '海口', '惠州', '珠海', '佛山', '东莞',
            '昆明', '重庆', '贵阳',
            '哈尔滨', '长春', '沈阳', '大连']
    dir = ['算法', '前端', '测试', '开发', '软件']
    cnt = [0, 0, 0, 0, 0, 0]
    i = 0
    # 爬虫名字
    name = 'work'

    n = 2
    # 设置访问域
    allowed_domains = ['jobui.com']
    # 开始连接 北京 软件
    start_urls = ['https://www.jobui.com/jobs?jobKw={}&cityKw={}&n={}'.format(dir[i], city[cnt[i]], 1)]
    # start_urls = ['https://www.jobui.com/jobs?jobKw=%E8%BD%AF%E4%BB%B6&cityKw=%E5%8C%97%E4%BA%AC&n=2']

    sleep_time = random.randint(1, 5) + random.random()
    time.sleep(sleep_time)

    # 薪水数据处理
    def salaryprocess(self, str):
        # xx千元每月
        if 'K/月' in str:
            salary = str.replace('K', '').replace('月', '').replace('/', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[1])) / 2 * 1000
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '

        if 'K' in str:
            salary = str.replace('K', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[1])) / 2 * 1000
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '
        elif '千元/月' in str:
            salary = str.replace('千元/月', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[1])) / 2 * 1000
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '
        elif '千/月' in str:
            salary = str.replace('千/月', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[1])) / 2 * 1000
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '
        elif '千元' in str:
            salary = str.replace('千元', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[1])) / 2 * 1000
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '
        elif '千' in str:
            salary = str.replace('千', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[1])) / 2 * 1000
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '

        elif '万元/月' in str:
            salary = str.replace('万元/月', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[1])) / 2 * 10000
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '
        elif '万/月' in str:
            salary = str.replace('万/月', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[1])) / 2 * 10000
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '

        elif '万元/年' in str:
            salary = str.replace('万元/年', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[1])) / 2 * 10000 / 12
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '
        elif '万/年' in str:
            salary = str.replace('万/年', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[1])) / 2 * 10000 / 12
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '


        elif '万元' in str:
            salary = str.replace('万元', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[0])) / 2 * 10000 / 12
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '
        elif '万' in str:
            salary = str.replace('万', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[0])) / 2 * 10000 / 12
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '


        elif '元/年' in str:
            salary = str.replace('元/年', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[0])) / 2 / 12
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '
        elif '元/月' in str:
            salary = str.replace('元/月', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[0])) / 2
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '
        elif '元' in str:
            salary = str.replace('元', '')
            salary = salary.split('-', 1)
            if len(salary) == 2:
                if salary[0].isdigit() & salary[1].isdigit():
                    salary = (float(salary[0]) + float(salary[0])) / 2
                    salary = round(salary, 2)
                    if salary > 50000.0:
                        return ' '
                    else:
                        return salary
            return ' '
        elif '面议' in str:
            return ' '
        return ' '

    def parse(self, response):
        # global n
        # 创建items实例
        time.sleep(0.5)
        item = WorkspiderItem()
        # print(response.body)

        works = response.xpath('//div[@class="c-job-list"]/div[@class="job-content-box"]')

        for each in works:

            occupation = each.xpath('div[@class="job-content"]/div[1]/a[@class="job-name"]/h3')
            if occupation:
                if '算法' in occupation.xpath('string(.)').extract()[0]:
                    item['occupation'] = '算法'
                elif '前端' in occupation.xpath('string(.)').extract()[0]:
                    item['occupation'] = '前端'
                elif '测试' in occupation.xpath('string(.)').extract()[0]:
                    item['occupation'] = '测试'
                elif '开发' in occupation.xpath('string(.)').extract()[0]:
                    item['occupation'] = '开发'
                elif ('软件' in occupation.xpath('string(.)').extract()[0] or '计算机' in
                      occupation.xpath('string(.)').extract()[0] or '互联网' in occupation.xpath('string(.)').extract()[
                          0] or 'IT' in occupation.xpath('string(.)').extract()[0] or '嵌入式' in
                      occupation.xpath('string(.)').extract()[0] or '程序' in
                      occupation.xpath('string(.)').extract()[0] or 'java' in
                      occupation.xpath('string(.)').extract()[0] or 'C++' in
                      occupation.xpath('string(.)').extract()[0] or 'php' in
                      occupation.xpath('string(.)').extract()[0] or 'python' in
                      occupation.xpath('string(.)').extract()[0] or 'Java' in
                      occupation.xpath('string(.)').extract()[0]):
                    item['occupation'] = '开发'
                else:
                    item['occupation'] = ' '

            item['location'] = self.city[self.cnt[self.i]]

            salary = each.xpath(
                'div[@class="job-content"]/div[2]/div[@class="job-desc"]/span[@class="job-pay-text"]/text()')
            if salary:
                item['salary'] = str(self.salaryprocess(salary.extract()[0]))

            if (self.salaryprocess(salary.extract()[0]) != ' ') & (item['occupation'] != ' '):
                yield item
        # 翻页
        nextLink = response.xpath('//div[@class="pager cfix"]/a[@class="pg-updown"][2]/@href').extract()
        if len(nextLink) > 0:
            yield scrapy.Request('https://www.jobui.com%s' % nextLink[0], callback=self.parse)

        # 换城市
        elif (self.cnt[self.i] < 39) & (self.i < 5):
            self.cnt[self.i] = self.cnt[self.i] + 1
            print(self.i)
            print(self.cnt)
            if (self.cnt[self.i] < 40):
                yield scrapy.Request(
                    'https://www.jobui.com/jobs?jobKw={}&cityKw={}&n={}'.format(self.dir[self.i],
                                                                               self.city[
                                                                                   self.cnt[self.i]],self.n),
                    callback=self.parse)
        # 换方向
        elif self.i < 4:
            self.i = self.i + 1
            yield scrapy.Request(
                'https://www.jobui.com/jobs?jobKw={}&cityKw={}&n={}'.format(self.dir[self.i],
                                                                           self.city[self.cnt[self.i]],self.n),
                callback=self.parse)
        # 爬下一页
        elif self.i < 6:

            self.i = 0
            self.n=self.n+1
            print(self.n)
            yield scrapy.Request(
                'https://www.jobui.com/jobs?jobKw=算法&cityKw={}&n={}'.format(
                    self.city[self.cnt[self.i]], self.n),
                callback=self.parse)
