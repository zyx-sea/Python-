# -----函數-------
#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

n1 = 255
n2 = 1000
print(hex(n1),hex(n2));

#数据类型检查可以用内置函数isinstance()实现
def nop(x,y,z):
    if not isinstance(int,int,int):
        raise TypeError('error')
    row=x+y+z;
    return row
nop(1,'dfs',4)

