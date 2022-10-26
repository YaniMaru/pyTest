
def get_list(n):
    res_list = []
    sum_res = 0
    for n in range(1, n + 1):
        res = (round((1 + 1 / n)**n, 2))
        sum_res += res
        res_list.append(res)
    sum_res = round(sum_res, 2)
    return sum_res


def multiply_pair_num(list1):
    result_list = []
    for i in range((len(list1) + 1) // 2):
        result_list.append(list1[i] * list1[len(list1) - 1 - i])
    return result_list


def binary(num):
    result = ''
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    return result


def sum_of_odd(my_list):
    res = 0
    for i in range(len(my_list)):
        if i % 2 != 0:
            res += my_list[i]
    return res


def fibonacci(num):
    fbn_num = []
    n1, n2 = 1, 1
    for _ in range(num):
        fbn_num.append(n1)
        n1, n2 = n2, n1 + n2
    n1, n2 = 0, 1
    for _ in range(num + 1):
        fbn_num.insert(0, n1)
        n1, n2 = n2, n1 - n2
    return fbn_num