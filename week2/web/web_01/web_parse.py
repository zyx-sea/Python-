from bs4 import BeautifulSoup

with open('F:/Python练习/week1/workhome_1/index.html','r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    print(Soup)