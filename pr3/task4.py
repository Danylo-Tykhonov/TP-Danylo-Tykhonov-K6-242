def find_insert_position(sorted_list, new_element):
    for i in range(len(sorted_list)):
        if new_element < sorted_list[i]:
            return i
    return len(sorted_list)

def test_insert_position():
    nums = [1, 3, 5, 7, 9]
    print("\nВідсортований список:", nums)
    x = int(input("Введи новий елемент: "))
    pos = find_insert_position(nums, x)
    print(f"Елемент {x} слід вставити на позицію {pos}")

test_insert_position()
