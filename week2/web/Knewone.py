from bs4 import BeautifulSoup
import requests
import time

url='https://knewone.com/things?page='

def get_page(url,data=None):    #批量爬取动态加载的数据

    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    # print(soup)
    imgs = soup.select('a.cover-inner > img')
    titles = soup.select('section.content > h4 > a')
    links = soup.select('section.content > h4 > a')

    if data==None:
        for img,title,link in zip(imgs,titles,links):
            data = {
                'img':img.get('src'),
                'title':title.get('title'),
                'link':link.get('href')
            }
            print(data)
def get_pages(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)       #时间保护，每次爬取停一秒
get_pages(1,10)      #爬取页数