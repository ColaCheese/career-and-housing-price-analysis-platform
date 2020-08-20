import scrapy
from soldHouse.items import SoldhouseItem


class HouseSpider(scrapy.Spider):
    # 爬虫名称
    name = "soldHouse"
    # 设置访问域
    allowed_domains = ['ke.com']
    # 开始链接
    citys = []
    secondcitys = []
    areas = []
    cityNum = 0
    areaNum = 0
    nowcitys = ["上海", "南京", "杭州", "合肥", "南昌", "福州", "济南", "宁波", "青岛", "无锡", "厦门", "烟台", "金华",
                "温州", "泉州", '长沙', "郑州", "武汉", "北京", "天津", "石家庄", "太原", "呼和浩特", "西安", "兰州",
                "银川", "广州", "海口", "惠州", "珠海", "佛山", "东莞", "成都", "昆明", "重庆", "贵阳", "哈尔滨", "长春",
                "沈阳", "大连"]
    print(len(nowcitys))
    start_urls = ['https://www.ke.com/city/']
    page = 1
    totalPage = 0

    # allcount = 0

    def parse(self, response):

        cityss = response.xpath('//div[@class="city_province"]/ul/li[@class="CLICKDATA"]/a/@href').extract()
        citynames = response.xpath('//div[@class="city_province"]/ul/li[@class="CLICKDATA"]/a/text()').extract()
        # print(cityss)
        # print(citysnames)

        for i in range(len(cityss)):
            if citynames[i] == "大洛杉矶地区":
                break
            if citynames[i] == "雄安新区":
                continue
            if str(self.nowcitys).find(citynames[i]) > 0:
                ccityurl = str(cityss[i])
                left = ccityurl.index("//")
                right = ccityurl.index(".")
                currentcityurl = ccityurl[left + 2:right]
                ife = ccityurl.find(".fang")
                if ife < 0:
                    city = (citynames[i], currentcityurl)
                    self.secondcitys.append(city)
                city = (citynames[i], currentcityurl)
                self.citys.append(city)

        print(self.citys)
        print(len(self.citys))
        print(self.secondcitys)
        print(len(self.secondcitys))

        # print(self.cityurl)
        # print(self.currentcity)
        # yield scrapy.Request('https://{}.ke.com/ershoufang/'.format(self.secondcitys[self.cityNum][1]),
        #                      callback=self.secondarea)

        yield scrapy.Request('https://{}.fang.ke.com/loupan/'.format(self.citys[self.cityNum][1]),
                             callback=self.newarea)

        # print(self.secondcitys)
        # print(len(self.secondcitys))
        # print(self.citys)
        # print(len(self.citys))
        # yield scrapy.Request('https://{}.fang.ke.com/loupan/'.format(self.citys[self.cityNum]), callback=self.newarea)

    def newarea(self, response):
        print("current city:")
        print(self.cityNum)
        self.areas = []
        self.areaNum = 0
        areass = response.xpath('//ul[@class="district-wrapper"]/li/@data-district-spell').extract()
        areanames = response.xpath('//ul[@class="district-wrapper"]/li/text()').extract()

        for i in range(len(areass)):
            area = (areanames[i], areass[i])
            self.areas.append(area)

        print(self.areas)

        yield scrapy.Request(
            'https://{}.fang.ke.com/loupan/{}/pg1'.format(self.citys[self.cityNum][1], self.areas[self.areaNum][1]),
            callback=self.newdetail)

        # print("area:{}".format(self.areas))
        # yield scrapy.Request(
        #    'https://{}.fang.ke.com/loupan/{}/pg1'.format(self.citys[self.cityNum], self.areas[self.areaNum]),
        #   callback=self.newdetail)

    def secondarea(self, response):
        print("current city:")
        print(self.cityNum)
        self.areas = []
        self.areaNum = 0
        areass = str(response.xpath('//div[@data-role="ershoufang"]/div/a/@href').extract())
        areasss = areass.split("/")
        areanames = response.xpath('//div[@data-role="ershoufang"]/div/a/text()').extract()
        j = 2
        for i in range(len(areanames)):
            area = (areanames[i], areasss[j])
            j += 3
            self.areas.append(area)
        print(self.areas)
        yield scrapy.Request(
            'https://{}.ke.com/ershoufang/{}/pg1'.format(self.secondcitys[self.cityNum][1],
                                                         self.areas[self.areaNum][1]),
            callback=self.seconddetail)


    def newdetail(self, response):

        # 创建items实例
        item = SoldhouseItem()

        allcount = response.xpath('//div[@class="page-box"]/@data-total-count').extract()[0]
        print("allcount:{}".format(allcount))
        self.totalPage = int(allcount) // 10 + 1
        # print("total:{}".format(totalPage))
        currentcount = 1
        houses = response.xpath('//div[@class="resblock-desc-wrapper"]')
        # print(houses)
        for each in houses:

            if allcount == '0':
                """
                item['name'] = "无"

                item['city'] = self.citys[self.cityNum][0]

                item['area'] = self.areas[self.areaNum][0]

                item['htype'] = "new"

                item['price'] = "0"

                item['allcount'] = allcount

                yield item
                """
                break

            if currentcount > int(allcount):
                break
            else:
                currentcount += 1

            # name = each.xpath('div[@class="resblock-name"]/a/text()').extract()
            # if name:
            #     item['name'] = name[0]

            item['city'] = self.citys[self.cityNum][0]

            item['area'] = self.areas[self.areaNum][0]

            item['htype'] = "new"

            price = each.xpath(
                'div[@class="resblock-price"]/div[@class="main-price"]/span[@class="number"]/text()').extract()
            unit = each.xpath(
                'div[@class="resblock-price"]/div[@class="main-price"]/span[@class="desc"]/text()').extract()
            # print(str(unit).find("总价"))
            print(price[0] == "价格待定")
            if str(unit).find("总价") != -1 or price[0] == "价格待定":
                continue
            if price:
                item['price'] = price[0]

            item['allcount'] = allcount

            yield item

        if self.page < self.totalPage:
            self.page += 1
            yield scrapy.Request(
                'https://{}.fang.ke.com/loupan/{}/pg{}'.format(self.citys[self.cityNum][1], self.areas[self.areaNum][1],
                                                               self.page), callback=self.newdetail)
        else:
            print("finished area:")
            print(self.areaNum)
            self.areaNum += 1
            if self.areaNum < len(self.areas):
                self.page = 1
                yield scrapy.Request(
                    'https://{}.fang.ke.com/loupan/{}/pg1'.format(self.citys[self.cityNum][1],
                                                                  self.areas[self.areaNum][1]), callback=self.newdetail)
            else:
                if self.cityNum < len(self.citys) - 1:
                    print(len(self.citys))
                    self.cityNum += 1
                    yield scrapy.Request(
                        'https://{}.fang.ke.com/loupan/'.format(self.citys[self.cityNum][1]), callback=self.newarea)
                else:
                    print("newall")
                    self.cityNum = 0
                    yield scrapy.Request('https://{}.ke.com/ershoufang/'.format(self.secondcitys[self.cityNum][1]),
                                         callback=self.secondarea)

    def seconddetail(self, response):

        # 创建items实例
        item = SoldhouseItem()

        allcount = str(response.xpath('//h2[@class="total fl"]/span/text()').extract()[0])
        # print(allcount)
        nextLink = str(response.xpath('//div[@class="page-box house-lst-page-box"]').extract())
        if int(allcount) > 0:
            left = nextLink.find("totalPage")
            right = nextLink.find("curPage")
            self.totalPage = int(nextLink[left + 11:right - 2])
        else:
            self.totalPage = 0
        currentcount = 1
        houses = response.xpath('//div[@class="info clear"]')
        for each in houses:
            if allcount == '0':
                break

            if currentcount > int(allcount):
                break
            else:
                currentcount += 1

            # name = each.xpath('div[@class="title"]/a/text()')
            # if name:
            #     item['name'] = name.extract()[0]

            item['city'] = self.secondcitys[self.cityNum][0]

            item['area'] = self.areas[self.areaNum][0]

            item['htype'] = "second"

            price = str(each.xpath(
                'div[@class="address"]/div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()').extract()[0])
            left = price.find("价")
            right = price.find("元")
            price = price[left + 1:right]
            # print(price)
            item['price'] = price

            item['allcount'] = allcount

            yield item

        if self.page < self.totalPage:
            self.page += 1
            yield scrapy.Request(
                'https://{}.ke.com/ershoufang/{}/pg{}'.format(self.secondcitys[self.cityNum][1],
                                                              self.areas[self.areaNum][1],
                                                              self.page), callback=self.seconddetail)
        else:
            print("finished area:")
            print(self.areaNum)
            self.areaNum += 1
            if self.areaNum < len(self.areas):
                self.page = 1
                yield scrapy.Request(
                    'https://{}.ke.com/ershoufang/{}/pg1'.format(self.secondcitys[self.cityNum][1],
                                                                 self.areas[self.areaNum][1]),
                    callback=self.seconddetail)
            else:
                if self.cityNum < len(self.secondcitys) - 1:
                    self.cityNum += 1
                    yield scrapy.Request(
                        'https://{}.ke.com/ershoufang/'.format(self.secondcitys[self.cityNum][1]),
                        callback=self.secondarea)
                else:
                    print("allcity")
