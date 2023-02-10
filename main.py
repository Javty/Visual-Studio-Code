# import modules
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Function


def said_hi():
    """ 
    A function that ask your name, and said hello

    Returns:
    Name
    """
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

def favorite():
    """ 
    A function that checks if the user cans guess my favorite food

    Returns:
    None
    """
    guess_food = input(print("What's my favorite food?"))
    if guess_food.lower() == "pizza":
        print("Yep! So amazing!")
    else:
        print("Tuck! That's not it!")
    print("Thanks! for playing!")
    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Maria = Person(said_hi(), "Chavez", 90, True)
    Maria.introduce()
    Toy = Dog("toby", "ball")
    Toy.play()
    favorite()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
