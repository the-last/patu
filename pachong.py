# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import time
from itertools import chain

def processDue(blocknum, blocksize, totalsize):
    '''''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%"% percent

def getHtml(url):
    request = urllib2.Request(url)
    # 区分服务器是否需要请求头，因为服务器需要判断请求来源是否为浏览器
    # if (url != 'https://news.baidu.com/' or url != 'https://www.qq.com/' or url != 'https://www.iqiyi.com/' ):  
    request.add_header('User-Agent','')
    
    response = urllib2.urlopen(request)
    html=response.read()
    # 本地存储
    # fl = open("/Users/kimoon/Documents/Python_/newsbaidu.html", 'a')
    # fl.write(html)
    # fl.close()
    # return html
    getImage(html, url)

def getImage(html, url):
    datalist=re.findall(r'data-original="(.*?.(jpg|jpeg|png|bmp))"', html)
    srclist=re.findall(r'src="(.*?.(jpg|webp|png|bmp))"', html)
    imglist=srclist
    if (len(datalist)>0):
        imglist = chain(datalist, srclist)
    
    print('##############################')
    print u"当前处理网址："
    print(url)
    print(imglist)
    # print(chain(datalist,srclist))
    print('##############################')
    for img in imglist:
        # 下载链接
        print(img[0], time.localtime(time.time()))
        location="/Users/kimoon/Documents/Python_/www/"
        uuu = img[0]
        if (img[0][0:4] != 'http'):
            uuu = 'http:'+img[0]
        
        urllib.urlretrieve(uuu, location + str(time.time()) + ".jpg", processDue)
        
        time.sleep(1)

if __name__=="__main__":
    getHtml("https://www.qq.com/")
    getHtml("https://www.iqiyi.com/")
    getHtml("https://www.taobao.com")
    getHtml("https://news.baidu.com/")
