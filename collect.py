import requests
import numpy as np
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

page_url = 'https://foreverblog.cn/feeds.html?page='  # 10年之约rss
number = 2592
titles = []


def collect_title(url):
    # 发送HTTP请求
    response = requests.get(url)

    # 解析HTML文档
    soup = BeautifulSoup(response.content, 'html.parser')
    # 使用正则表达式匹配
    articles = soup.findAll('article', class_='post')
    for article in articles:
        titles.append(article.h1.text.strip('\n\n'))
    print(url+'已经采集完成')

def saveArray(array):
    arr = np.array(array)
    np.savetxt('titles.txt',arr,fmt='%s',encoding='utf-8')
    print('保存所有标题完毕！')

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(collect_title,page_url+str(i+1)) for i in range(number)]
        for f in futures:
            f.result()

    print(len(titles))
    saveArray(titles)



