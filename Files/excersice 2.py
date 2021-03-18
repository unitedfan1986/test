def get_range_numbers(begin: int, end: int, even: bool = True) -> list:
    my_list = []
    for num in range(begin, end):
        if even:
            if num % 2 == 0:
                my_list.append(num)
        else:
            my_list.append(num)
    return my_list


range_list = get_range_numbers(1, 10)
print(range_list)

range_list = get_range_numbers(1, 10, False)
print(range_list)
