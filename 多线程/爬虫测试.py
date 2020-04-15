import threading
import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import pdb


img_queue = Queue()
pdb.set_trace()
x = 10
url = "http://www.doutula.com/photo/list/?page=%d" % x
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
response = requests.get(url, headers=headers)
text = response.text
html = etree.HTML(text)
imgs = html.xpath("//div[@class='page-content text-center']//a//img")
for img in imgs:
    if img.get('class') == 'gif':
        continue
    img_url = img.xpath(".//@data-original")[0]
    suffix = os.path.splitext(img_url)[1]
    alt = img.xpath(".//@alt")[0]
    alt = re.sub(r'[，。？?,/\\·]', '', alt)
    img_name = alt + suffix
    img_queue.put((img_url, img_name))