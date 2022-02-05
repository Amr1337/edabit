# https://edabit.com/challenge/6nSckbgCx9hjTwmcw
from datetime import datetime


def time_for_milk_and_cookies(date):
    return date == datetime.date(date.year, 11, 24)

'''
import datetime

time_for_milk_and_cookies(datetime.date(2013, 12, 24)), True
time_for_milk_and_cookies(datetime.date(3000, 12, 24)), True
time_for_milk_and_cookies(datetime.date(2013, 1, 23)), False
time_for_milk_and_cookies(datetime.date(2010, 11, 2)), False
time_for_milk_and_cookies(datetime.date(1980, 9, 24)), False'''