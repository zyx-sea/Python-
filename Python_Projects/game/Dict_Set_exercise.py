
#-----------dict-------
student={'name':'Tom','sex':'man','age':21}
print(student['name'])  #注意格式

student['phone']=17854333333
print(student['phone'])  #添加

student.pop('sex')
print(student) #删除

# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

#---------------Set--------------
s=set([1,2,4,4,4,5,3])
print(s)  #注意格式，内部值不可重复

s.add(6)
print(s) #添加
s.remove(6)
print(s) #删除


