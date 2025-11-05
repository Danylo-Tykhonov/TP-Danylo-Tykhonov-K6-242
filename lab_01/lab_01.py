students = [
    {"name": "Bob",  "phone": "0631234567", "email": "bob@gmail.com",  "address": "Kyiv"},
    {"name": "Emma", "phone": "0632345678", "email": "emma@gmail.com", "address": "Lviv"},
    {"name": "Jon",  "phone": "0633456789", "email": "jon@gmail.com",  "address": "Odesa"},
    {"name": "Zak",  "phone": "0634567890", "email": "zak@gmail.com",  "address": "Kharkiv"}
]

def printAllList():
    print("\nСПИСОК СТУДЕНТІВ:")
    for elem in students:
        print(f"{elem['name']}: {elem['phone']}, {elem['email']}, {elem['address']}")
    print() 
    return

def addNewElement():
    print("\n=== Додавання нового студента ===")
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть телефон: ")
    email = input("Введіть email: ")
    address = input("Введіть адресу: ")

    newItem = {"name": name, "phone": phone, "email": email, "address": address}

    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)

    print("Новий запис додано!\n")
    return

def deleteElement():
    print("\n=== Видалення студента ===")
    name = input("Введіть ім'я студента для видалення: ")

    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break

    if deletePosition == -1:
        print("Студента не знайдено.\n")
    else:
        del students[deletePosition]
        print(f"Студента '{name}' видалено.\n")
    return

def updateElement():
    print("\n=== Оновлення інформації ===")
    name = input("Введіть ім'я студента, якого потрібно оновити: ")

    updatePosition = -1
    for item in students:
        if name == item["name"]:
            updatePosition = students.index(item)
            break

    if updatePosition == -1:
        print("Студента не знайдено.\n")
        return

    current = students[updatePosition]
    print("Введіть нові дані (Enter — щоб залишити старе значення):")

    new_name = input(f"Ім'я [{current['name']}]: ") or current['name']
    new_phone = input(f"Телефон [{current['phone']}]: ") or current['phone']
    new_email = input(f"Email [{current['email']}]: ") or current['email']
    new_address = input(f"Адреса [{current['address']}]: ") or current['address']

    updated_item = {
        "name": new_name,
        "phone": new_phone,
        "email": new_email,
        "address": new_address
    }

    del students[updatePosition]

    insertPosition = 0
    for item in students:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, updated_item)

    print("Інформацію оновлено!\n")
    return

def main():
    while True:
        choice = input("Оберіть дію [C - додати, U - оновити, D - видалити, P - показати, X - вихід]: ")

        match choice.lower():
            case "c":
                addNewElement()
                printAllList()
            case "u":
                updateElement()
                printAllList()
            case "d":
                deleteElement()
                printAllList()
            case "p":
                printAllList()
            case "x":
                print("Програму завершено.")
                break
            case _:
                print("Невірна команда, спробуйте ще раз.\n")

if __name__ == "__main__":
    main()
