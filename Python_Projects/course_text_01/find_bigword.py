#-----------找出文档中出现频率最高单词和它出现的次数——————
from pip._vendor.distlib.compat import raw_input
name=raw_input('Enter file:')
handle=open(name,'r')
text=handle.read()
words=text.split()  #通过指定分隔符对字符串进行切片，默认为空格，返回值为字符串列表

counts=dict()  #dict()内置字典
for word in words:
    counts[word]=counts.get(word,0)+1
bigcount=None
bigword=None

for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)

