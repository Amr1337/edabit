# https://edabit.com/challenge/QgSMSMpfcEebAyCye

def time_saved(speed_limit, avg_speed, d_traveled):

    time_speed_limit = d_traveled / speed_limit
    time_avg_speed = d_traveled / avg_speed

    # multiply by 60 to convert from hours to minutes
    delta_time = (time_speed_limit - time_avg_speed) * 60

    print(round(delta_time, 1))

time_saved(80, 90, 40)
time_saved(80, 90, 4000)
time_saved(80, 100, 40)
time_saved(80, 100, 10)
'''
time_saved(80, 90, 40), 3.3)
time_saved(80, 90, 4000), 333.3)
time_saved(80, 100, 40), 6.0)
time_saved(80, 100, 10), 1.5)
time_saved(60, 65, 25), 1.9)
time_saved(60, 60, 20), 0)
time_saved(80, 95, 200), 23.7)
time_saved(70, 92, 50), 10.2)
time_saved(70, 92, 20), 4.1)
time_saved(70, 100, 12), 3.1)
'''