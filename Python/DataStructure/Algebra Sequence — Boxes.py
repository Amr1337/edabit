# https://edabit.com/challenge/baBNZFCozmjNhbp9Q

def box_seq(step):
    if step == 0:
        return 0
    box = 3
    for i in range(2, step + 1):
        if i % 2 == 0:
            box -= 1
        else:
            box += 3
    return box


print(box_seq(5))
print(box_seq(0))
print(box_seq(6))
print(box_seq(99))
print(box_seq(2))
print(box_seq(1))
'''
box_seq(5), 7)
box_seq(0), 0)
box_seq(6), 6)
box_seq(99), 101)
box_seq(2), 2)
box_seq(1), 3)

'''
