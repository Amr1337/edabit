# https://edabit.com/challenge/93o8dzshnn2fDHdpX

def lst_ele_sum(l):
    """
    # solving using list comprehension
    [sum(l)- i for i in l]
    """

    ''' # another aspect to solve it w/ less code
     x= sum(l) -l[i]
     l_sum.append(x)
    sum_of_items = 0'''

    l_sum = []
    for i in range(len(l)):
        sum_of_items = 0
        for j in l:
            sum_of_items += j
        sum_of_items -= l[len(l_sum)]
        l_sum.append(sum_of_items)

    return l_sum


print(lst_ele_sum([1, 2, 3, 2, 1]))  # ➞ [8, 7, 6, 7, 8]
print(lst_ele_sum([1, 2]))
print(lst_ele_sum([1, 2, 3]))
print(lst_ele_sum([10, 20, 30, 40, 50, 60]))
'''
lst_ele_sum([1, 2]), [2, 1])
lst_ele_sum([1, 2, 3]),  [5, 4, 3])
lst_ele_sum([1, 2, 3, 4, 5]), [14, 13, 12, 11, 10])
lst_ele_sum([10, 20, 30, 40, 50, 60]),  [200, 190, 180, 170, 160, 150])
'''
