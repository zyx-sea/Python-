# ---------------- List--------------------
friends = ['xiaoming', 'xiaopeng', 'xiaoli']  # list有序集合
print(friends);

print(len(friends));  # list元素个数

print(friends[2]);
print(friends[0]);
print(friends[-1]);  # list类似c语言的数组可以用索引来查看list，-1也可以做索引

friends.append('tom')
print(friends);  # 添加元素向list里面
friends.insert(0, 'Zhou');
print(friends);  # 插入元素
friends.pop();
print(friends);  # 只能从末尾上删除元素
friends.pop(1);
print(friends);  # 根据索引删除元素
friends = ['Zhou', 1, friends, True];
print(friends);  # list里面的元素的数据类型也可以不同,list元素也可以是另一个list

# _______________________________tuple_____________________
t = (1, 2, 3)
print(t);  # 一旦定义不可修改，但是可以覆写
t = ()
print(t)  # 表示空值

t = ('a', 'b', ['a', 'b']);
t[2][0] = 'X';
t[2][1] = 'Y';
print(t);  # “可变的”tuple

# _____________________练习————————————————————————
# ————————————————————请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    ];
print( L[0][0],'\n',L[1][1],'\n',L[2][2]);
