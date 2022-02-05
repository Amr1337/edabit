# https://edabit.com/challenge/p88k8yHRPTMPt4bBo

def count_vowels(txt):
    count = 0

    return sum(1 for i in txt if i.lower() in "aeiou")

''' vowls = ['a', 'e', 'i', 'o', 'u']
    for i in txt:
        if i in vowls:
            count += 1
    return count'''
