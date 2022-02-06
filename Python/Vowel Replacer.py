# https://edabit.com/challenge/Ggq8GtYPeHJQg4v7q

def replace_vowels(word, c):
    vowels = "aieou"
    for i in word.lower():
        if i in vowels:
            new_string = word.replace(i, c)
    print(new_string)

replace_vowels("the aardvark", "#")
replace_vowels("minnie mouse", "?")
replace_vowels("shakespeare", "*")
replace_vowels("all is fair in love and war", "<")

'''
replace_vowels("the aardvark", "#"), "th# ##rdv#rk"
replace_vowels("minnie mouse", "?"), "m?nn?? m??s?"
replace_vowels("shakespeare", "*"), "sh*k*sp**r*"
replace_vowels("all is fair in love and war", "<"), "<ll <s f<<r <n l<v< <nd w<r"
'''