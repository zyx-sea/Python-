from bs4 import BeautifulSoup
import requests

url='http://bj.xiaozhu.com/fangzi/8765474364.html'
web_data=requests.get(url)
soup=BeautifulSoup(web_data.text,'lxml')
# print(soup)

names=soup.select('div.pho_info > h4 > em')[0].text
locations=soup.select('div.pho_info > p > span')[0].text
prices=soup.select('div.day_l > span')[0].text
imags=soup.select('#curBigImage')[0].get('src')
fimages=soup.select('div.member_pic > a > img')[0].get('src')
fsexs=soup.select('div.member_pic > div')[0].get('class')[0]
fnames=soup.select('a.lorder_name')[0].text

# print(names)
# print(locations)
# print(prices)
# print(imags)
# print(fimages)
# print(fsexs)
# print(fnames)

def print_gender(class_sex):
    if(class_sex=='member_ico'):
        return '男'
    else:
        return '女'

data={
        '房名':names,
        '位置':locations,
        '价格':prices,
        '房子图片':imags,
        '房主头像':fimages,
        '房主性别':print_gender(fsexs),
        '房主名字':fnames
}
print(data)