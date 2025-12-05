import csv
import sys


def load_csv(file_name):
    list_students = []
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                list_students.append(row)
        print("Data loaded successfully!")
        return list_students
    except FileNotFoundError:
        print("File not found!")
        return []

def save_csv(file_name, list_students):
    with open(file_name, 'w', newline='') as file:
        fieldnames = ["name", "phone", "email", "group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in list_students:
            writer.writerow(student)

def printAllList(list_students):
    for elem in list_students:
        print(f"Student name is {elem['name']}, Phone is {elem['phone']}, Email: {elem['email']}, Group: {elem['group']}")

def addNewElement(list_students):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    group = input("Enter group: ")

    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    pos = 0
    for s in list_students:
        if newItem["name"] > s["name"]:
            pos += 1
        else:
            break

    list_students.insert(pos, newItem)
    print("New element added!")


def deleteElement(list_students):
    name = input("Enter name to delete: ")

    for i, elem in enumerate(list_students):
        if elem["name"] == name:
            list_students.pop(i)
            print("Element deleted!")
            return

    print("Element not found!")


def updateElement(list_students):
    name = input("Enter name to update: ")

    for i, elem in enumerate(list_students):
        if elem["name"] == name:
            print("Leave field empty to keep old value.")

            new_name = input(f"New name ({elem['name']}): ") or elem["name"]
            new_phone = input(f"New phone ({elem['phone']}): ") or elem["phone"]
            new_email = input(f"New email ({elem['email']}): ") or elem["email"]
            new_group = input(f"New group ({elem['group']}): ") or elem["group"]

            updated = {
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "group": new_group
            }

            
            list_students.pop(i)

            pos = 0
            for s in list_students:
                if updated["name"] > s["name"]:
                    pos += 1
                else:
                    break

            list_students.insert(pos, updated)

            print("Element updated!")
            return

    print("Student not found!")


def main():
    if len(sys.argv) < 2:
        print("Please provide the file name as a command line argument!")
        return

    file_name = sys.argv[1]
    data = load_csv(file_name)

    while True:
        choice = input("\nChoose action [C create, U update, D delete, P print, X exit]: ")

        match choice.lower():
            case "c":
                addNewElement(data)
            case "u":
                updateElement(data)
            case "d":
                deleteElement(data)
            case "p":
                printAllList(data)
            case "x":
                save_csv(file_name, data)
                print("CSV saved. Exit.")
                break
            case _:
                print("Wrong choice!")


if __name__ == '__main__':
    main()