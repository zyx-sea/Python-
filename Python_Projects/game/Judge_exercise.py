# ----------if语句-----------
age = 14
if age > 18:
    print("你已经是成年人了！！")
else:  # 注意此处的“：”与C不同的是，条件不用（）而是在其后加上 ：
    if age < 13:
        print("你还是个小孩子！！")  # else if 还可以简写成elif
    else:
        print("你应该上中学了吧！！")

x = 3
if x:
    print('true')
else:
    print('flase')  # if判断条件还可以简写

age = input("输入你的年龄：")
age = int(age)  # 注意变量的类型
if age > 18:
    print("你已经是成年人了！！")
else:  # 注意此处的“：”与C不同的是，条件不用（）而是在其后加上 ：
    if age < 13:
        print("你还是个小孩子！！")  # else if 还可以简写成elif
    else:
        print("你应该上中学了吧！！")

# -----------练习-----------
#
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：
h = 1.75
w = 80.5
bmi = 80.5 / 1.75 / 1.75
if bmi < 18.5:
    print("小明的体重过轻！！")
elif 18.5 < bmi < 25:
    print("小明的体重正常！！")
elif 25 < bmi < 28:
    print("小明的体重过重！！")
elif 28 < bmi < 32:
    print("小明的体重肥胖！！")
elif 32 < bmi:
    print("小明的体重严重肥胖！！")

# --------循环--------
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)  # 方法一

sum = 0
for x in [1, 2, 3, 4, 5, 6]:
    sum = sum + x;
print(sum)

sum = 0
for x in range(101):
    sum = sum + x;
print(sum)


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)     #方法二，更灵活些

# 练习
# 请利用循环依次对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello,',name)