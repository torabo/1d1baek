def solution(num_list, n):
    list1 = num_list[n:]
    list2 = num_list[:n]
    answer = list1 + list2
    return answer