import urllib
url = 'http://www.freebuf.com/articles'
globalcontent = urllib.urlopen(url).read()
news_start = globalcontent
count = 1

while count <= 16:
    try:
        news_inner_head = news_start.find('<dt><a href=')
        news_inner_tail = news_start.find('.html')
        news_inner_url = news_start[news_inner_head + 13:news_inner_tail + 5]
        print(news_inner_url)
        news_start = news_start[news_inner_tail + 5:]

        filename = news_inner_url[-10:]
        urllib.urlretrieve(news_inner_url, filename)
        count += 1
    except:
        print
        'Download Success!'
    finally:
        if count == 16:
            break
