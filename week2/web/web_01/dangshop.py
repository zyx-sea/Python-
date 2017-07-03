from bs4 import BeautifulSoup
import requests

url='http://product.dangdang.com/1470715853.html'
web_data=requests.get(url)
soup=BeautifulSoup(web_data.text,'lxml')
# print(soup)

imags=soup.select('main-img-slider > li.on > a > img')





data={

        '图片':imags
}
print(data)