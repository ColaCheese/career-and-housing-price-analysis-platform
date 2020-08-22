import math
import scrapy
import time
import random
from ..items import WorkspiderItem


class WorkSpider1(scrapy.Spider):
    city = ['北京', '上海', '广州', '成都', '武汉',
            '南京', '杭州', '合肥', '南昌', '福州', '济南', '宁波', '青岛', '无锡', '厦门', '烟台', '金华', '温州', '泉州',
            '长沙', '郑州', '天津', '石家庄', '呼和浩特', '太原',
            '西安', '兰州', '银川',
            '海口', '惠州', '珠海', '佛山', '东莞',
            '昆明', '重庆', '贵阳',
            '哈尔滨', '长春', '沈阳', '大连']
    cnt = 0
    # 爬虫名字
    name = 'work1'
    # 设置访问域
    allowed_domains = ['liepin.com']
    # 开始连接 北京 软件
    start_urls = ['https://www.liepin.com/zhaopin/?isAnalysis=&dqs=010&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=638a297842fe53eb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=638a297842fe53eb&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EF5FSJAXvyHmQyODXqGxdVw&d_sfrom=search_prime&d_ckId=fc5664c0fd66d7e775821dbe6a41d4b4&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99']

    sleep_time = random.randint(1, 5) + random.random()
    time.sleep(sleep_time)

    def salaryprocess(self, str):
        # xx千元每月
        if '万' in str:
            salary = str.replace('万', '')
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
        elif '面议' in str:
            return ' '
        return ' '

    def parse(self, response):
        # 创建items实例
        time.sleep(0.5)
        item = WorkspiderItem()
        # print(response.body)

        works = response.xpath('//li/div[@class="sojob-item-main clearfix"]')
        for each in works:
            occupation = each.xpath('div[@class="job-info"]/h3/a/text()')
            if occupation:
                if ('软件' in occupation.extract()[0] or '互联网' in occupation.extract()[0] or '计算机' in occupation.extract()[0] or 'IT' in occupation.extract()[0] or '程序' in occupation.extract()[0] or 'Android' in occupation.extract()[0] or 'java' in occupation.extract()[0] or 'Java' in occupation.extract()[0] or 'c++' in occupation.extract()[0] or 'C++' in occupation.extract()[0] or 'Python' in occupation.extract()[0] or '嵌入式' in occupation.extract()[0]):
                    if '算法' in occupation.extract()[0] :
                        item['occupation'] = '算法'
                    elif '前端' in occupation.extract()[0] :
                        item['occupation'] = '前端'
                    elif '测试' in occupation.extract()[0] :
                        item['occupation'] = '测试'
                    else:
                        item['occupation'] = '开发'
                else:
                    item['occupation'] = ' '

            item['location'] = self.city[self.cnt]

            salary = each.xpath('div[@class="job-info"]/p[@class="condition clearfix"]/span[@class="text-warning"]/text()')
            if salary:
                item['salary'] = str(self.salaryprocess(salary.extract()[0]))

            if (self.salaryprocess(salary.extract()[0]) != ' ')&(item['occupation'] != ' ') :
                yield item

        c = response.xpath('//div[@class="pagerbar"]/a[@class="current"]/text()').extract()[0]
        nextLink = response.xpath('//div[@class="pagerbar"]/a[2]/@href').extract()

        if int(c) > 1:
            yield scrapy.Request('https://www.liepin.com%s' % nextLink[0], callback=self.parse)

        else:
            #上海
            if (self.cnt == 0):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=8139c9589aab5106&compkind=&fromSearchBtn=2&sortFlag=15&ckid=8139c9589aab5106&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7Er3i1HcfrfE3VRWBaGW6LoA&d_sfrom=search_prime&d_ckId=3ca8dd6a5bc6e3078ae838147fd3fcfb&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #广州
            elif (self.cnt == 1):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=050020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=add90a36177c3dae&compkind=&fromSearchBtn=2&sortFlag=15&ckid=add90a36177c3dae&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7E_FrslumzzaHrHe3aSW0VTQ&d_sfrom=search_prime&d_ckId=5e25bb50cd9d8325db96b4226dc74be3&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            # 成都
            elif (self.cnt == 2):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=280020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=add90a36177c3dae&compkind=&fromSearchBtn=2&sortFlag=15&ckid=72cc593f2c600218&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EDARaeHgTI7JY9N3sNhM1Ow&d_sfrom=search_prime&d_ckId=3bc53345287d00771d2c613df64c8985&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #武汉
            elif (self.cnt == 3):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=170020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=add90a36177c3dae&compkind=&fromSearchBtn=2&sortFlag=15&ckid=967391ece02dd162&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EILIFxAzMuTzzOU47n1bPhg&d_sfrom=search_prime&d_ckId=3cf63c8f631ebb64ea22e237a74b5612&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #南京
            elif (self.cnt == 4):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=060020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=fb07ef97875703cd&compkind=&fromSearchBtn=2&sortFlag=15&ckid=fb07ef97875703cd&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7ERvRIXdBmEWt_E5g9cNGr2g&d_sfrom=search_prime&d_ckId=55ab02ca57ddd573b57017990071f0d5&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #杭州
            elif (self.cnt == 5):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=070020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=fb07ef97875703cd&compkind=&fromSearchBtn=2&sortFlag=15&ckid=56bd10a2bc329943&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7Eb82XZEfT3k9nLaGd2nO5lg&d_sfrom=search_prime&d_ckId=3b35009db5dcb177bb6cee3a9f6749d3&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #合肥
            elif (self.cnt == 6):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=080020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=fb07ef97875703cd&compkind=&fromSearchBtn=2&sortFlag=15&ckid=50bd5d0e7cdcb2ed&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EysbGUosKFmVGOcoIeAerpA&d_sfrom=search_prime&d_ckId=44dfa1c3c65b885d0e6b0d059f25f8e0&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #南昌
            elif (self.cnt == 7):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=200020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=fb07ef97875703cd&compkind=&fromSearchBtn=2&sortFlag=15&ckid=307813cff8b82281&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7ElbRMnu6a52JCQy8colByCQ&d_sfrom=search_prime&d_ckId=8ef9928bbfdb6b0ea259084f7990f585&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=93',callback=self.parse)
            #福州
            elif (self.cnt == 8):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=090020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=fb07ef97875703cd&compkind=&fromSearchBtn=2&sortFlag=15&ckid=e059836488f362e4&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7Edn9-wmNXi6arg8DQRa38Aw&d_sfrom=search_prime&d_ckId=6712c1c26155545d34aa6e2f7f874587&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #济南
            elif (self.cnt == 9):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=250020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=fb07ef97875703cd&compkind=&fromSearchBtn=2&sortFlag=15&ckid=d8726e1ee557f277&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EzNjQxHHCnHFOcoMw-1L49g&d_sfrom=search_prime&d_ckId=59f32e36973c14e946b612c5440d6ea8&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #宁波
            elif (self.cnt == 10):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=070030&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=fb07ef97875703cd&compkind=&fromSearchBtn=2&sortFlag=15&ckid=0df063b0d159b6c6&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7E8gC6CfYcd8Ye3BMMjgu6pg&d_sfrom=search_prime&d_ckId=c684467708c93ffc043aede823649e38&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #青岛
            elif (self.cnt == 11):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=250070&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=fb07ef97875703cd&compkind=&fromSearchBtn=2&sortFlag=15&ckid=5737799e3b91eea0&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EVNlrTKGSH9rbZaebUQ5A7Q&d_sfrom=search_prime&d_ckId=f97869c5ec787dac7abd1d4c404704d1&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #无锡
            elif (self.cnt == 12):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=060100&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=fb07ef97875703cd&compkind=&fromSearchBtn=2&sortFlag=15&ckid=7bfaa3601f4c2d1e&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7ETH-qePnaW1jaFAQtiFMdmg&d_sfrom=search_prime&d_ckId=2ee3b9da6dff8cf73044a38706230f31&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #厦门
            elif (self.cnt == 13):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=090040&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=fb07ef97875703cd&compkind=&fromSearchBtn=2&sortFlag=15&ckid=4ce9e5eecb973623&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EA0uZ0t7iX4E2almcFOmlRw&d_sfrom=search_prime&d_ckId=d3d54c33939776554ddb9f08a681ce7d&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #烟台
            elif (self.cnt == 14):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=250120&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=fb07ef97875703cd&compkind=&fromSearchBtn=2&sortFlag=15&ckid=63a7b8d894e43293&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7ESSvHWxUiVLk6kQ7e0omT2w&d_sfrom=search_prime&d_ckId=b369b353677fceeb5c634f241626b25d&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=35',callback=self.parse)
            #金华
            elif (self.cnt == 15):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=070060&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=fb07ef97875703cd&compkind=&fromSearchBtn=2&sortFlag=15&ckid=18da49aee9ea08b3&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EhLmAhMdC7w5dIxXXW4y-qA&d_sfrom=search_prime&d_ckId=7fa11fe954a39b2015de2d6d8fab315f&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=40',callback=self.parse)
            #温州
            elif (self.cnt == 16):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=070040&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=cbff3c2aa4d912bb&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7E1aS1LIUJeP3cevnS4c3d6A&d_sfrom=search_prime&d_ckId=29ad7c3896f04fb1b0e78746a2fcf52a&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=61',callback=self.parse)
            #泉州
            elif (self.cnt == 17):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=090030&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=af192ab3dfdf03d4&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EbyiMRwiaJaCutgflwrghnQ&d_sfrom=search_prime&d_ckId=cf1de77463ba1c4e07346e429f6e7252&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=38',callback=self.parse)
            #长沙
            elif (self.cnt == 18):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=180020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=44d003bb6bf057a7&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EvRNk79t3knxSK8e8osSaWQ&d_sfrom=search_prime&d_ckId=7a960abf72ca718c5b62126fb47ca76d&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #郑州
            elif (self.cnt == 19):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=150020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=fbb8083df5805ff1&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7E-Gw6taVFUG4CWqViHEM79A&d_sfrom=search_prime&d_ckId=4f89dd0afec1e2f3c115539143cfa4c8&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #天津
            elif (self.cnt == 20):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=030&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=fa7c5eaa25163a5e&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EtaNTg2NIXYd3H-ywTj62JQ&d_sfrom=search_prime&d_ckId=d526c9d917a0c9b6ac8c6aa55a36105e&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #石家庄
            elif (self.cnt == 21):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=140020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=3240f505d3105b01&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EhcZJginJBmT91BFh6EUemQ&d_sfrom=search_prime&d_ckId=e1491b8825a222a531f8d69c08823d20&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=73',callback=self.parse)
            #呼和浩特
            elif (self.cnt == 22):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=220020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=d3c03316068ad2c1&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EOAxzwZX_cwZtBJKl3XQ3Ew&d_sfrom=search_prime&d_ckId=441689ca70fb3dfa909991ab06506a78&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=24',callback=self.parse)
            #太原
            elif (self.cnt == 23):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=260020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=b8578a4adfd70d3f&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EoWoNihOiWgGg9E_7cju3sg&d_sfrom=search_prime&d_ckId=228c5caa5108536eb7d221424344ecbd&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=48',callback=self.parse)
            #西安
            elif (self.cnt == 24):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=270020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=416dbdffa13e10b5&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7E12hwLHP5WlpLPGyv_8q2Iw&d_sfrom=search_prime&d_ckId=7e9710bb8279373d64a8fdc6c90b23cf&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #兰州
            elif (self.cnt == 25):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=100020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=6486c26824f00a7f&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EZq8XW8fQD2Ro1N0ci9adKA&d_sfrom=search_prime&d_ckId=88b999903b013dcc4d0dd5c44180d428&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=26',callback=self.parse)
            #银川
            elif (self.cnt == 26):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=230020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=57b9eff8964812af&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7ExHhUpXpvRmmHilFwFl4d_Q&d_sfrom=search_prime&d_ckId=843b5b66bafb6dc702b48ca77d52e654&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=17',callback=self.parse)
            #海口
            elif (self.cnt == 27):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=130020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=affd0be073b0ca45&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7El4Q5lGxkU-CLSWLgddBlhg&d_sfrom=search_prime&d_ckId=22af36ab0fa42b84338a7d0b56d84828&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=34',callback=self.parse)
            #惠州
            elif (self.cnt == 28):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=050060&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=9ff6ba94aadf69ee&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7ElISM6_bb3LnryRT9JZC1Wg&d_sfrom=search_prime&d_ckId=1281450ee0ef395a113443e5d68d6d06&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=64',callback=self.parse)
            #珠海
            elif (self.cnt == 29):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=050140&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=d6a0f41e363a7172&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EFFavi9xYj5_d4o8MhqFp3g&d_sfrom=search_prime&d_ckId=9e5613d522d83d49bd0f3f639cb4bd74&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #佛山
            elif (self.cnt == 30):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=050050&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=c8be880e5a02ab1a&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7E_QTOB92PhSyUvWbXhyuqjg&d_sfrom=search_prime&d_ckId=17c585efedc31b93ff39a488a4d58c1e&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #东莞
            elif (self.cnt == 31):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=050040&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=a2f41f5ab81f96b8&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EER1bginubgxeQzYQLAUKgQ&d_sfrom=search_prime&d_ckId=27b99008c44fc42782af128b20a2702f&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #昆明
            elif (self.cnt == 32):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=310020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=60e9c81faeaf45cd&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EVQRSKBRLn38ATumhqtvMAA&d_sfrom=search_prime&d_ckId=b1580f841f5d9577962e4722da737de6&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=91',callback=self.parse)
            #重庆
            elif (self.cnt == 33):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=040&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=f04e374fc26304fd&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EDnIK07pheM0dUfyGVexLMQ&d_sfrom=search_prime&d_ckId=57e2b1962fcb3019c10a359fed63bace&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=99',callback=self.parse)
            #贵阳
            elif (self.cnt == 34):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=120020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=ab3d63cda9f3fb42&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7E1Tzdbk8-Y2Xm--MdgNNfyA&d_sfrom=search_prime&d_ckId=52d3f4034c94327b184e18ded591719e&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=65',callback=self.parse)
            #哈尔滨
            elif (self.cnt == 35):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=160020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=b5008ef2e643bab0&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7Epl0kgmzkWZ0m6HORJ_8Nwg&d_sfrom=search_prime&d_ckId=be92171ce7d162a4243782b0650fdf2c&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=36',callback=self.parse)
            #长春
            elif (self.cnt == 36):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=190020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=159ae093c90ffd17&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EAeDJK93fZxqFBOaNRxYdXw&d_sfrom=search_prime&d_ckId=e13ac64a4d1c74279301941a098b0f9f&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=54',callback=self.parse)
            #沈阳
            elif (self.cnt == 37):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=210020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=caa6e5568836c932&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EAm8Ih1iTrVlJqLmceHgCqw&d_sfrom=search_prime&d_ckId=ac7b93e26867ea6ead581757e5287311&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=92',callback=self.parse)
            #大连
            elif (self.cnt == 38):
                self.cnt += 1
                yield scrapy.Request('https://www.liepin.com/zhaopin/?isAnalysis=&dqs=210040&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E8%BD%AF%E4%BB%B6&init=-1&searchType=1&headckid=cbff3c2aa4d912bb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=043511e4ba9e85e0&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=8N_GW3Hw9MB1An7L_mbvfA%7EdSsSNtRUg09tgzsv7oykKQ&d_sfrom=search_prime&d_ckId=a61b9eb4db990a35601c16f45bdfdcb6&d_curPage=0&d_pageSize=40&d_headId=a0f698096ef6e9d70a51c519a2b5cef6&curPage=91',callback=self.parse)
            else:
                    print('finish')
