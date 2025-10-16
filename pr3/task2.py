def test_list_functions():
    nums = [3, 1, 4]
    print("Початковий список:", nums)

    nums.append(5)
    print("append(5):", nums)

    nums.extend([7, 8])
    print("extend([7,8]):", nums)

    nums.insert(1, 9)
    print("insert(1,9):", nums)

    nums.remove(4)
    print("remove(4):", nums)

    copy_nums = nums.copy()
    print("copy():", copy_nums)

    nums.sort()
    print("sort():", nums)

    nums.reverse()
    print("reverse():", nums)

    nums.clear()
    print("clear():", nums)

test_list_functions()
