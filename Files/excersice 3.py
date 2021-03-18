import random

random.randint(1, 20)


def random_list(begin: int, end: int, amount: int, exclude: list = None):
    temp_list = []
    for i in range(0, amount):
        random_number = random.randint(begin, end)
        while random_number in exclude:
            random_number = random.randint(begin, end)
        temp_list.append(random_number)

    return temp_list


rnd_list = random_list(1, 20, 10, [4, 1])
print(rnd_list)
