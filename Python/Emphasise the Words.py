# https://edabit.com/challenge/K5277r6RmsJRSz27t

def emphasise(str):
    new_word = ""
    c = []
    str = str.lower()
    for i in range(len(str)):
        if i == 0:
            c.append(str[i].capitalize())
            continue
        if str[i-1].isspace():
            c.append(str[i].capitalize())
            continue
        c.append(str[i])
    new_word = "".join(c)
    print(new_word)


emphasise("hello world")
emphasise("GOOD MORNING")
emphasise("99 red balloons!")
emphasise("1 2 3 4 5 6 7 8 9")
emphasise("")
emphasise("joshua senoron")
'''
emphasise("hello world"), "Hello World")
emphasise("GOOD MORNING"), "Good Morning")
emphasise("99 red balloons!"), "99 Red Balloons!")
emphasise("1 2 3 4 5 6 7 8 9"), "1 2 3 4 5 6 7 8 9")
emphasise(""), "")
emphasise("joshua senoron"), "Joshua Senoron")pan.")
'''