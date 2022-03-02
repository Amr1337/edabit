# https://edabit.com/challenge/McZF4JRhPus5DtRA4

def dna_to_rna(dna):
    rna_bases = "UACG"
    dna_bases = "ATGC"
    table = dna.maketrans(dna_bases, rna_bases)
    return dna.translate(table)


print(dna_to_rna("ATTAGCGCGATATACGCGTAC"))
print(dna_to_rna("CGATATA"))
print(dna_to_rna("GTCATACGACGTA"))


'''
dna_to_rna("GCGTAC"), "CGCAUG")
dna_to_rna("ATTAGCGCGATATACGCGTAC"), "UAAUCGCGCUAUAUGCGCAUG")
dna_to_rna("CAGTATGCTGCAT"), "GUCAUACGACGUA")
dna_to_rna("CGATATA"), "GCUAUAU")
dna_to_rna("GCAGCTACA"), "CGUCGAUGU")
'''