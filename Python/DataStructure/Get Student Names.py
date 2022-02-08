# https://edabit.com/challenge/HvkPdhijquecKASdF

def get_student_names(d):
    l = list(d.values())
    l.sort()
    return l


print(get_student_names({
    "Student 1": "Steve",
    "Student 2": "Becky",
    "Student 3": "John"
}))

print(get_student_names({
    "Student 1": "Jacek",
    "Student 2": "Ewa",
    "Student 3": "Zygmunt",
    "Student 4": "Tomek"
}))
