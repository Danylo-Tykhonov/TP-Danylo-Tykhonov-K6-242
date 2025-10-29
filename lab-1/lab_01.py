def print_menu():
    print("\n=== Телефонний довідник студентів ===")
    print("1. Додати нового студента")
    print("2. Змінити дані про студента")
    print("3. Видалити запис")
    print("4. Показати всі записи")
    print("5. Вихід")
    print("=====================================")

def print_students(students):
    if not students:
        print("Довідник порожній.")
        return

    print("\n--- Список студентів ---")
    print(f"{'№':<3} {'Ім’я':<20} | {'Телефон':<12} | {'Email':<25} | {'Група'}")
    print("-" * 70)
    for i, s in enumerate(students, start=1):
        print(f"{i:<3} {s['name']:<20} | {s['phone']:<12} | {s['email']:<25} | {s['group']}")
    print("-" * 70)

def add_student(students):
    name = input("Введіть ім'я студента: ").strip()
    phone = input("Введіть телефон: ").strip()
    email = input("Введіть email: ").strip()
    group = input("Введіть групу: ").strip()

    students.append({"name": name, "phone": phone, "email": email, "group": group})
    students.sort(key=lambda s: s["name"].lower())
    print(f"Студента {name} додано.")

def find_student(students, name):
    name = name.lower()
    matches = [s for s in students if name in s["name"].lower()]
    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        print("Знайдено кілька збігів:")
        for i, s in enumerate(matches, start=1):
            print(f"{i}. {s['name']}")
        idx = input("Оберіть номер потрібного студента: ")
        if idx.isdigit() and 1 <= int(idx) <= len(matches):
            return matches[int(idx) - 1]
    return None

def edit_student(students):
    name = input("Введіть ім'я студента, якого потрібно змінити: ").strip()
    student = find_student(students, name)
    if not student:
        print("Студента не знайдено.")
        return

    print(f"\nПоточні дані:")
    print(f"Ім’я: {student['name']}")
    print(f"Телефон: {student['phone']}")
    print(f"Email: {student['email']}")
    print(f"Група: {student['group']}")

    print("\nЯкщо не хочете змінювати певне поле — залиште його порожнім.")
    new_phone = input("Новий телефон: ").strip()
    new_email = input("Новий email: ").strip()
    new_group = input("Нова група: ").strip()

    if new_phone:
        student["phone"] = new_phone
    if new_email:
        student["email"] = new_email
    if new_group:
        student["group"] = new_group

    students.sort(key=lambda s: s["name"].lower())
    print(f"Дані студента {student['name']} оновлено.")

def delete_student(students):
    name = input("Введіть ім'я студента для видалення: ").strip()
    student = find_student(students, name)
    if student:
        students.remove(student)
        students.sort(key=lambda s: s["name"].lower())
        print(f"Студента {student['name']} видалено.")
    else:
        print("Студента не знайдено.")

def main():
    students = [
        {"name": "Тихонов Данило", "phone": "xxxxxxxx", "email": "ihor@example.com", "group": "TP-KB-22-1"},
        {"name": "Олена Сидоренко", "phone": "0637654321", "email": "olena@example.com", "group": "TP-KB-22-2"},
    ]

    while True:
        print_menu()
        choice = input("Оберіть дію (1-5): ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            edit_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            print_students(students)
        elif choice == "5":
            print("Вихід з програми")
            break
        else:
            print("Невірний вибір")

if __name__ == "__main__":
    main()
