def test_dict_functions():
    print("\nТестування функцій словників")
    student = {"name": "Danylo", "age": 18}
    print("Початковий словник:", student)

    student.update({"grade": "A"})
    print("update({'grade': 'A'}):", student)

    del student["age"]
    print("del age:", student)

    print("keys():", list(student.keys()))
    print("values():", list(student.values()))
    print("items():", list(student.items()))

    student.clear()
    print("clear():", student)

test_dict_functions()
