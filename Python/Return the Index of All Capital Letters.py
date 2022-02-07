# https://edabit.com/challenge/rQkriLJBc9CbfRbJb

def index_of_caps(str):
    print([i for i in range(len(str)) if str[i].isupper()])

index_of_caps("eDaBiT")
index_of_caps("eQuINoX")
index_of_caps("determine")
index_of_caps("STRIKE")
index_of_caps("sUn")
index_of_caps("SpiDer")
index_of_caps("accOmpAnY")
index_of_caps("@xCE#8S#i*$en")
index_of_caps("1854036297")
index_of_caps("Fo?.arg~{86tUx=|OqZ!")
'''
index_of_caps("eDaBiT"), [1, 3, 5])
index_of_caps("eQuINoX"), [1, 3, 4, 6])
index_of_caps("determine"), [])
index_of_caps("STRIKE"), [0, 1, 2, 3, 4, 5])
index_of_caps("sUn"), [1])
index_of_caps("SpiDer"), [0, 3])
index_of_caps("accOmpAnY"), [3, 6, 8])
index_of_caps("@xCE#8S#i*$en"), [2, 3, 6])
index_of_caps("1854036297"), [])
index_of_caps("Fo?.arg~{86tUx=|OqZ!"), [0, 12, 16, 18])
'''