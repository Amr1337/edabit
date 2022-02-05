# https://edabit.com/challenge/8pDH2SRutPoaQghgc

def relation_to_luke(name):
    solutions = {'Leia': 'sister',
                 'Darth Vader': 'father',
                 'Han': 'brother in law',
                 'R2D2': 'droid'}
    return 'Luke, I am your {}.'.format(solutions[name])


'''relation_to_luke("Darth Vader"), "Luke, I am your father."
relation_to_luke("Leia"), "Luke, I am your sister."
relation_to_luke("Han"), "Luke, I am your brother in law."
relation_to_luke("R2D2"), "Luke, I am your droid."
'''
