# coding=utf-8
#a<z<0<9<A<Z
import string

def sort_list(test_list):
    '''
    整体思路，按照给定的顺序给每个字母一个从大到小的值，计算出第一个值之后，字母也添加上值，但是这个时候需要添加权重，index越大，权重越小，小到不会影响超过下一个不相同的字符
    当前方法的bug：如果一个字符串的长度特别长的时候，position_weight的字典需要特别大，但是我是手动制定了1000
    '''
    letters = string.ascii_lowercase+string.digits+string.ascii_uppercase
    #每个位置一个分数，按照给定的排序顺序
    score_dict = {letters[i]:i for i in range(len(letters))}

    #位置的分数，第二位的字母开始，每个字的加上分数乘以权重
    position_weight = {i:(i+1)*0.01 for i in range(1000)}

    final_score = []
    for i in test_list:
        temp_list = [i,score_dict[i[0]]]  #第一个位置的分数，放入一个列表
        temp_i = i[1:]
        for j in temp_i: #遍历从第二个开始的每一个字母，分数乘以权重
            temp_list[1] += score_dict[j]*position_weight[temp_i.index(j)]
        final_score.append(temp_list)

    final_score = sorted(final_score,key=lambda x:x[1],reverse=False)
    ret = [i[0] for i in final_score]
    return ret

if __name__ == '__main__':
    test_list = ["258", "AAb", "ddd", "ab", "AA", "d", "AAA", "dd", "1111"]
    print(sort_list(test_list))