# https://edabit.com/challenge/R5F99DeuhqYxbGyMM

def word_builder(chars, pos):
    new_word = ""
    # chars =["g", "e", "o"]
    # pos = [1, 0, 2]
    for i in pos:
        new_word += "".join(chars[i])
    print(new_word)


word_builder(["g", "e", "o"], [1, 0, 2])
word_builder(["e", "t", "s", "t"], [3, 0, 2, 1])
word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2])
word_builder(["l", "e", "h", "n", "l", "c", "a", "e", "g"], [5, 2, 6, 4, 0, 1, 3, 8, 7])
word_builder(["s", "o", "r", "t", "e", "d"], [0, 1, 2, 3, 4, 5])
'''
word_builder(["g", "e", "o"], [1, 0, 2]), 'ego')
word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]), 'test')
word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]), 'edabit')
word_builder(["l", "e", "h", "n", "l", "c", "a", "e", "g"], [5, 2, 6, 4, 0, 1, 3, 8, 7]), 'challenge')
word_builder(["s", "o", "r", "t", "e", "d"], [0, 1, 2, 3, 4, 5]), 'sorted')
'''