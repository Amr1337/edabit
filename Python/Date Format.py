# https://edabit.com/challenge/co4nwXSvnCjGEu8vp


def format_date(date):
    new_date = date.rsplit("/")
    print(new_date[2]+new_date[1]+new_date[0])


format_date("11/12/2019")
format_date("12/31/2019")
format_date("01/15/2019")

'''
format_date("11/12/2019") ➞ "20191211"

format_date("12/31/2019") ➞ "20193112"

format_date("01/15/2019") ➞ "20191501"
'''