# https://edabit.com/challenge/S9KCN5kqoDbhNdKh5

def count_characters(lst):
    count = 0
    for i in lst:
        *j, = i
        count += len(j)
    return count


print(count_characters([
'###',
'###',
'###'
]))
print(count_characters([
'22222222',
'22222222',
]))

print(count_characters([
'------------------'
]))

print(count_characters([]))
print(count_characters([
'',
'']))

'''
count_characters([
'###',
'###',
'###'
]), 9)

count_characters([
'22222222',
'22222222',
]), 16)

count_characters([
'------------------'
]), 18)

count_characters([]), 0)
count_characters([
'',
'']), 0)
'''