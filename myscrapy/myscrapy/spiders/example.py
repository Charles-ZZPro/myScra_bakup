# -*- coding: utf-8 -*-
import scrapy
import hashlib
# from tutorial.items import JinLuoSiItem
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
import os
import sys
reload(sys)  
sys.setdefaultencoding('utf8') 

class DmozSpider(scrapy.Spider):
    name = "tacgpr"    #唯一标识，启动spider时即指定该名称
    allowed_domains = ["tacgpr.com"]
    start_urls = [
        # "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        # "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/"
        "http://www.tacgpr.com/index.html",
        "http://www.tacgpr.com/about.html",
        "http://www.tacgpr.com/service.html",
        "http://www.tacgpr.com/case.html",
        "http://www.tacgpr.com/join.html",
        "http://www.tacgpr.com/contact.html",

        # "http://www.johnsoncontrols.com/zh_cn"
    ]

    def parse(self, response):
        # for sel in response.xpath("//div[@class='title-and-desc']"):
        #     title = sel.xpath("a/div[@class='site-title']/text()").extract()
        #     link = sel.xpath("a/@href").extract()
        #     desc = sel.xpath("div[@class='site-descr ']/text()").extract()
        #     print title, link, desc
        current_url = response.url #爬取时请求的url
        body = response.body  #返回的html
        unicode_body = response.body_as_unicode()#返回的html unicode编码
        # print unicode_body

        # os.mkdir('/home/charles/johnson/')
        # os.mknod('/home/charles/johnson/'+current_url) 
        name = current_url[7:]
        name = name.replace("/","$$$")

        fp = open(name,'w')
        fp.write(unicode_body)
        fp.close()


        # 分析页面
        # 找到页面中符合规则的内容（校花图片），保存
        # 找到所有的a标签，再访问其他a标签，一层一层的搞下去

        hxs = HtmlXPathSelector(response)#创建查询对象

        # # 如果url是 http://www.xiaohuar.com/list-1-\d+.html
        # if re.match('http://www.xiaohuar.com/list-1-\d+.html', response.url): #如果url能够匹配到需要爬取的url，即本站url
        #    items = hxs.select('//div[@class="item_list infinite_scroll"]/div') #select中填写查询目标，按scrapy查询语法书写
        #    for i in range(len(items)):
        #        src = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()#查询所有img标签的src属性，即获取校花图片地址
        #        name = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % i).extract() #获取span的文本内容，即校花姓名
        #        school = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract() #校花学校
        #        if src:
        #            ab_src = "http://www.xiaohuar.com" + src[0]#相对路径拼接
        #            file_name = "%s_%s.jpg" % (school[0].encode('utf-8'), name[0].encode('utf-8')) #文件名，因为python27默认编码格式是unicode编码，因此我们需要编码成utf-8
        #            file_path = os.path.join("/Users/wupeiqi/PycharmProjects/beauty/pic", file_name)
        #            urllib.urlretrieve(ab_src, file_path)        

        # 获取所有的url，继续访问，并在其中寻找相同的url
        all_urls = hxs.select('//a/@href').extract()
        for url in all_urls:
            if url.startswith('http://www.tacgpr.com/'):
                yield Request(url, callback=self.parse)            

