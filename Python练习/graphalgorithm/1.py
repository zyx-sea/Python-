def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1         # list[mid]值不是想要的值，在左区间
        else:
            low = mid + 1          # list[mid]值不是想要的值，在右区间
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))  # 找到，地址为1,索引从0开始
print(binary_search(my_list, -1))  # 没找到，返回none
