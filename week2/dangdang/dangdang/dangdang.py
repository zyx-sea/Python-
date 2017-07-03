from bs4 import BeautifulSoup
import requests
import urllib.request

urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-{}'.format(str(i)) for i in range(1,26)]

def get_info(url):
	wd_data = requests.get(url)
	soup = BeautifulSoup(wd_data.text,'lxml')

	ids = soup.select('div.list_num')
	names = soup.select('div.name a')
	images = soup.select('div.pic  a img')
	# sibling_soup = BeautifulSoup(str(soup.select('ul.bang_list.clearfix.bang_list_mode > li')),'lxml')
	authors = soup.select('div.publisher_info > a:nth-of-type(1)')
	ls = [a.get('title') for a in authors if a.get('title') != None ]
	for number,name,image,author in zip(ids,names,images,[a.get('title').split('\u3000') for a in authors if a.get('title') != None ]):
		data = {
		'id':number.get_text().split('.')[0],
		'name':name.get_text(),
		'author':author,
		'image':image.get('src')
		}
		print(data)

	
	

for url in urls :
	get_info(url)
