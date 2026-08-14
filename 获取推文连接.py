# -*- coding:utf-8 -*- 
import requests
import json
import re
import random
import time

with open("cookies.txt", "r") as file:
    cookie = file.read()
cookies = json.loads(cookie)
# url = "https://mp.weixin.qq.com"
# response = requests.get(url, cookies=cookies)
token = '46420669'  # 从url中获取token
print(token)
proxies = {
    "http": None,
    "https": None,
}
headers = {
    "Cookie": "appmsglist_action_3916864453=card; pgv_pvid=8150591040; ptcz=e6951daf987aac864b515e5edb1df4fdc83092d472b460f3fa06b9f9e35c4df1; _qimei_q36=; _qimei_h38=e147effa2a7d8cddc9b3882702000008b1811e; fopenid=F365F1A35FB8543EFEB46F8E3683C194; token=72B3774C626C68E454016D61E1CC8413; it_c=0; eas_sid=N117T2v3b0H2u8P2g1B1I553R5; LW_uid=B1O7c2d4090323L7j110A5Z705; ua_id=3UcvT6u2He5XPjtQAAAAANwdjUbn5F2bCclq-DpE-hU=; wxuin=30265234632819; mm_lang=zh_CN; RK=p4kgaY7mFy; LW_sid=K1H7T4U6z0k1h6h9G193P4L7X1; rewardsn=; wxtokenkey=777; _clck=3916864453|1|fvl|0; uuid=37ba99466a10806df38ec1de2f426bc0; rand_info=CAESIOg03Ujhrpg+4t/0w9WDBMDom7rqgL+hKTu+RDhcOMN1; slave_bizuin=3916864453; data_bizuin=3916864453; bizuin=3916864453; data_ticket=lwhCiANNBCE5iJHQIg5kSgvDs0juBAi5FgNQJmBcKP31euOEem5nXxdKOMmcjvru; slave_sid=cUhxRUlGOFpwN0xhRnVCS3Ja3Q0VERPVWIwdVdq0hGejVFQ1NydGwzQ3NhUUVGcjQ5MWpTYUZrRlNQZlNQYVZDeWl6NjdZSUd4RE53cGV0V3RtZHhDQzU2T0N5bFFQenA2cWUwUGRUa2x6WVM0TlJ5NWs2M0xpckx5Z08yT2pHNWlyV3piSE53WTFWY2Nw; slave_user=gh_d9f630e0f2c6; xid=8928cd8a07b9b9513a90cb7aac30b18c; _clsk=10mnszo|1746260305579|5|1|mp.weixin.qq.com/eheat-agent/payload/record",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Referer": "https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&token=" + token + "&lang=zh_CN",
    "Host": "mp.weixin.qq.com",
}

# requestUrl = "https://mp.weixin.qq.com/cgi-bin/searchbiz" str(begin)
with open('new_article_link_2.txt', "a", encoding='utf-8') as file:
    for j in range(448, 484, 1):
        begin = (j - 1) * 5
        requestUrl = "https://mp.weixin.qq.com/cgi-bin/appmsgpublish?sub=list&search_field=null&begin=" + str(
            begin) + "&count=5&query=&fakeid=MzU1ODIwNjQ0MQ%3D%3D&type=101_1&free_publish_type=1&sub_action=list_ex&fingerprint=b9202bd699bf3b48820cb2a6dffac2b9&token=" + str(
            token) + "&lang=zh_CN&f=json&ajax=1"
        search_response = requests.get(requestUrl, cookies=cookies, headers=headers, proxies=proxies)
        re_text = search_response.json()
        # print(re_text)
        list = json.loads(re_text.get("publish_page"))
        print(list)
        for item in list["publish_list"]:
            # print(item) 1730390400
            if item["publish_info"] == '': continue
            publish_info = json.loads(item["publish_info"])
            for publish_info_item in publish_info["appmsgex"]:
                # if publish_info_item["update_time"] > 1730390400:
                file.write(
                    publish_info_item["aid"] + "<=====>" + publish_info_item["title"] + "<=====>" + publish_info_item[
                        "link"] + "<=====>" + str(publish_info_item["update_time"]) + "\n")
                print(publish_info_item["aid"] + "<=====>" + publish_info_item["title"] + "<=====>" + publish_info_item[
                    "link"] + "<=====>" + str(publish_info_item["update_time"]))
                print(j)

        # print(time.strftime("%Y-%m-%d", list[0]["update_time"]))
        # for i in list:
        #     t = time.strftime("%Y-%m-%d", time.localtime(i["update_time"])).split("-")
        #     print(t)
        #     if t[0] == '2024' and t[1] == '11':
        #         file.write(i["aid"] + "<=====>" + i["title"] + "<=====>" + i["link"] + "\n")
        #         print(i["aid"] + "<=====>" + i["title"] + "<=====>" + i["link"])
        time.sleep(2)
