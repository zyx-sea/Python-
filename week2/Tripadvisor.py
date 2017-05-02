#--------爬取旅游网信息
from bs4 import BeautifulSoup
import requests

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_SORT_WRAPPER'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text,'lxml')
# print(soup)   #整个网页结构
titles = soup.select('#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.listing_title > a[target="_blank"]')
# print(titles) #相关一类信息
imgs= soup.select('img[width="180"]')
#print(titles,imgs) #一类信息的图片
categorys = soup.select('#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.tag_line > div > a')
#print(categorys)  #分类别

#装入字典中
for title,img,cate in zip(titles,imgs,categorys):
    data = {
        'title':title.get_text(),
        'img':img.get('src'),
        'cate':list(cate.stripped_strings),
    }
    print(data)
