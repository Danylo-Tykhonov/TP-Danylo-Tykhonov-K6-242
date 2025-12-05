students_data = [
    {'name': 'Daria', 'grade': 73},
    {'name': 'Ivan', 'grade': 89},
    {'name': 'Svitlana', 'grade': 94},
    {'name': 'Taras', 'grade': 58},
    {'name': 'Roman', 'grade': 81},
    {'name': 'Yulia', 'grade': 100},
    {'name': 'Bohdan', 'grade': 66},
    {'name': 'Iryna', 'grade': 77},
    {'name': 'Serhii', 'grade': 91},
    {'name': 'Nadia', 'grade': 84}
]


while True:
    c = input("Select the column by which you want to sort information about students(name, grade): ")
    if c == "name" or c == "grade":
        break
    else:
        print("\nYou entered something wrong in the name of the column to be sorted. Please, try again!!!\n")

def sort_dicts(list, name_col):
    sorted_dict = sorted(list, key=lambda dict: dict[name_col])
    if name_col == "grade":
        print("\nSorted by grade\n")
        sorted_dict.reverse()
        for col in sorted_dict:
            print(f'{col["name"]} {col["grade"]}')
    else:
        print("\nSorted by name\n")
        for col in sorted_dict:
            print(f'{col["name"]} {col["grade"]}')

sort_dicts(students_data, c)