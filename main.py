# import modules
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Function


def said_hi():
    # Use a breakpoint in the code line below to debug your script
    print("Hi ¿What is your name?")
    name = input()
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    return name


class Dog:
    def __init__(self, name, favorite_toy):
        self.name = name
        self.favorite_toy = favorite_toy

    def play(self):
        print(self.name + " is playing with the " + self.favorite_toy)


class Person:
    # Class example
    def __init__(self, firstname, lastname, age, status):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.status = status

    def introduce(self):
        print(f"my name is {self.firstname} {self.lastname} I am  {self.age} my status is {self.status}")


Maria = Person(said_hi(), "Chavez", 90, True)
Toy = Dog("toby", "ball")
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # said_hi()
    Maria.introduce()
    Toy.play()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
