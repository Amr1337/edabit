# https://edabit.com/challenge/Cjtm4CpLzHDerQMfX


def area_of_country(name, area):
    world_landmass = 148940000
    country_percentage = (area / world_landmass) * 100
    # return f"{name} is {round(country_percentage, 2)}% of total world's landmass"
    return "{} is {:.2f}% of total world's landmass".format(name, country_percentage)


print(area_of_country("Russia", 17098242))
print(area_of_country("USA", 9372610))
print(area_of_country("Iran", 1648195))


'''
area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass")
area_of_country("Russia", 17098242), "Russia is 11.48% of the total world's landmass")
area_of_country("Iran", 1648195), "Iran is 1.11% of the total world's landmass")
area_of_country("India", 3287590), "India is 2.21% of the total world's landmass")
area_of_country("China", 9706961), "China is 6.52% of the total world's landmass")
area_of_country("Yemen", 527968), "Yemen is 0.35% of the total world's landmass")
area_of_country("Switzerland", 41284), "Switzerland is 0.03% of the total world's landmass")
'''