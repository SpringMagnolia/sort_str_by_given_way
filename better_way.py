import operator
import string

def insert_sort(lists):
    # 冒泡排序
    for i in range(len(lists)):
        for j in range(i+1,len(lists)):
            if operator.gt(lists[i][1],lists[j][1]):
                lists[i],lists[j] = lists[j],lists[i]
    return lists

def my_compare(my_list):
    '''
    整体思路：使用operater中提供额gt和lt等方法，能够直接比较字符串或者是列表的大小，对列表是比较其中从前往后的数字的大小
    同时配合常见的排序方式来完成排序
    '''
    letters = string.ascii_lowercase + string.digits + string.ascii_uppercase
    # 每个位置一个分数，按照给定的排序顺序
    score_dict = {letters[i]: i for i in range(len(letters))}

    temp_list = []
    for i in my_list:
        temp_dict = [i,[score_dict[j] for j in i]]
        temp_list.append(temp_dict)
    temp_list = insert_sort(temp_list)
    ret = [i[0] for i in temp_list]
    return ret


if __name__ == '__main__':
    test_list = ["258", "AAb", "ddd", "ab", "AA", "d", "AAA", "dd", "1111"]
    ret = my_compare(test_list)
    print(ret)