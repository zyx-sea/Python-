import  urllib.request ,urllib.response

host = 'http://saweather.market.alicloudapi.com'
path = '/area-to-id'
method = 'GET'
appcode = '7793711114fc4bbfb424f818eef8e7e2'
querys = 'area=青岛'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.urlopen(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib.response.urlopen(request)
content = response.read()
if (content):
    print(content)