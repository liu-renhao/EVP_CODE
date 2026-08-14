import json
import re
import time
from bs4 import BeautifulSoup
import requests
import os

proxies = {
    "http": None,
    "https": None,
}

# 获得登录所需cookies
with open("cookies.txt", "r") as file:
    cookie = file.read()
cookies = json.loads(cookie)
# url = "https://mp.weixin.qq.com"
# response = requests.get(url, cookies=cookies, proxies=proxies)
# token1 = re.findall(r'token=(\d+)', str(response.url))
# print(token1)
# token = token1[0]
# print(token)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Referer": "https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=12&token=" + 'zwNVgGUndJN0hgVUAAAAGwbMr9MesdBoQmEeu8L__Hw=' + "&lang=zh_CN",
    "Host": "mp.weixin.qq.com",
}
# f = open("article_link.txt", encoding='utf-8')  # 返回一个文件对象
# line = f.readline()  # 调用文件的 readline()方法
# for line in open("article_link.txt", encoding='UTF-8'):
# new_line = line.strip()
# line_list = new_line.split("<=====>")
# file_name = line_list[0]
# dir_name = line_list[1]
# requestUrl = 'https://mp.weixin.qq.com/s/oEwPrw4YLY_nc_vqnZUmRA'

with open('new_article_link_re.txt', "r", encoding='utf-8') as file:
    t = file.read()
    rt = t.split("\n")
    for i in rt:
        ii = i.split("<=====>")
        requestUrl = ii[1]
        search_response = requests.get(requestUrl, cookies=cookies, headers=headers, proxies=proxies)
        soup = BeautifulSoup(search_response.text, 'lxml')
        print(ii[1])

        # # 提取内容
        # content_element = soup.find('div', {'class': 'rich_media_content'})
        # if content_element:
        #     content = content_element.decode_contents()
        # else:
        #     content = "内容未找到"
        #     break

        # soup.find('section').decompose()  # 去头
        # print(soup.get_text())
        r1 = soup.select("table tr")

        with open('new_result.csv', "a", encoding='utf-8-sig') as file1:
            #  写入转成字符串的字典

            for r1i in r1:
                r2 = []
                r1s = r1i.select("span")
                for r1si in r1s:
                    r2.append(r1si.get_text())
                    res = ",".join(r2)
                file1.write(ii[2] + ',' + res + '\n')
# with open('result1.html', "w", encoding='utf-8') as file:
#     #  写入转成字符串的字典
#     file.write(content)



# print("----------------下载完毕：" +"----------------下载完毕：" + requestUrl)
# time.sleep(2)
# file.close()