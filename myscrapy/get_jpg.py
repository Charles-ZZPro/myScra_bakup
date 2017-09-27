#coding=utf-8

#urllib模块提供了读取Web页面数据的接口
import urllib
#re模块主要包含了正则表达式
import re
#定义一个getHtml()函数
def getHtml(url):
    print "opening !!"
    page = urllib.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    print "got!!"
    print page
    html = page.read() #read()方法用于读取URL上的数据
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'    #正则表达式，得到图片地址
    print reg
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
    print imglist
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0

    for imgurl in imglist:
        imgurl = "http://www.tacgpr.com/"+imgurl
        sel = imgurl.split("/")
        print imgurl
        ppp = sel[-1]
        print ppp
        # imgurl = "http://johnson.miso-lab.com" + imgurl
        urllib.urlretrieve(imgurl,'/home/charles/workspace/scra_ali/myscrapy/%s' % ppp)
        x+=1


html = getHtml("http://www.tacgpr.com/index.html")
# print html
print getImg(html)