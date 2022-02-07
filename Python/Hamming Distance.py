# https://edabit.com/challenge/nfWirHJzNRBMAp9Df


def hamming_distance(str1, str2):
    diffs = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            diffs +=1
    return diffs

print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))



'''
hamming_distance("abcde", "bcdef") ➞ 5

hamming_distance("abcde", "abcde") ➞ 0

hamming_distance("strong", "strung") ➞ 1
'''