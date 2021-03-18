class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def say(self):
        return f'Hi, I am {self.__class__.__name__} {self.name} and I am {self.age}'


class Zebra(Animal):
    pass


class Dolphin(Animal):
    pass




d = Dolphin("Chuck", 20)
z = Zebra("Zelda", 30)

print(d.say)
print(z.say