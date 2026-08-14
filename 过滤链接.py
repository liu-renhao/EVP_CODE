import time


def exchange(timeStamp):
    # 给定一个时间戳
    # timeStamp = 1557502800

    # 转换为time.struct_time对象
    timeArray = time.localtime(timeStamp)

    # 格式化为字符串
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)

    return otherStyleTime


with open('new_article_link_1.txt', "r", encoding='utf-8') as file:
    t = file.read()
with open('new_article_link_2.txt', "r", encoding='utf-8') as file:
    p = file.read()
with open('new_article_link_re.txt', "w", encoding='utf-8') as file:
    rt = t.split("\n")
    rp = p.split("\n")
    sum = 0
    for i in rt:
        if len(i) == 0: break
        ii = i.split("<=====>")
        if (ii[1].find("招") > 0 or ii[1].find("聘用") > 0 or ii[1].find("聘") > 0) and (ii[1].find("招生") < 0 and ii[1].find("公示") < 0):
            print(ii)
            sum = sum + 1
            if len(ii) > 2:
                file.write(ii[1] + "<=====>" + ii[2] + "<=====>" + exchange(int(ii[3])) + '\n')
    for i in rp:
        if len(i) == 0: break
        ii = i.split("<=====>")
        if (ii[1].find("招") > 0 or ii[1].find("聘用") > 0 or ii[1].find("聘") > 0) and (ii[1].find("招生") < 0 and ii[1].find("公示") < 0):
            print(ii)
            sum = sum + 1
            if len(ii) > 2:
                file.write(ii[1] + "<=====>" + ii[2] + "<=====>" + exchange(int(ii[3])) + '\n')


print(sum)
