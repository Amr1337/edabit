# https://edabit.com/challenge/7RPtGySfZLkEHB8ac

def wash_hands(N, nM):
    duration_day = (N * 21) / 60  # duration in minutes
    duration_overall = duration_day * 30 * nM

    print("{} minutes and {} seconds".format(int(duration_overall), int(duration_overall % 1 * 60)))


wash_hands(8, 7)
wash_hands(20, 10)
wash_hands(7, 9)
wash_hands(0, 2)
wash_hands(13, 3)
wash_hands(1, 1)
wash_hands(7, 0)

'''
wash_hands(8, 7),  "588 minutes and 0 seconds")
wash_hands(20, 10), "2100 minutes and 0 seconds")
wash_hands(7, 9),  "661 minutes and 30 seconds")
wash_hands(0, 2),  "0 minutes and 0 seconds")
wash_hands(13, 3), "409 minutes and 30 seconds")
wash_hands(1, 1), "10 minutes and 30 seconds")
wash_hands(7, 0), "0 minutes and 0 seconds")
'''