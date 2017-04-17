from bs4 import BeautifulSoup
import requests

url = 'http://www.tuniu.com/g38632/pkg-all-0/'
wy_data = requests.get(url)
soup=BeautifulSoup(wy_data.text,'lxml')
# titles=soup.select('')
print(soup)

