# https://edabit.com/challenge/uKPc5faEzQkMwLYPP

from math import ceil


def end_corona(recovers, new_cases, active_cases):
    return ceil(active_cases / (recovers - new_cases))


'''Test cases:
end_corona(4000, 2000, 77000), 39)
end_corona(3000, 2000, 50699), 51)
end_corona(30000, 25000, 390205), 79)
end_corona(260000, 255000, 20511691), 4103)'''