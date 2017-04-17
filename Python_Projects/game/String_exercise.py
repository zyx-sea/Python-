# -------------------字符串和编码--------------------
print('中文和english'); #python编码为Unicode，支持多种语言
print(ord('A'));#获取字符的整数表示
print(chr(65));#将编码转换成相应的字符
print('abc'.encode('ascii'));#encode()将字符串转换成byte
print('中文'.encode('utf-8'));
print('中文'.encode('ascii'));#中文编码超过ascii编码范围
'hello,%s'%'kk' #%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。

# -----------练习-----------------
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
score1 = 72;
score2 = 85;
ratio = score2 / score1 - 1
print('%.1f' % ratio);
