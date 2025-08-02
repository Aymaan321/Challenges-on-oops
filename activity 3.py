import random

class Fruit_quiz:
    def __init__(self):
        self.fruits = {"Apple": "red", 
                       "Banana": "yellow",
                       "Durian": "white",
                       "Grapes": "purple",
                       "Watermelon": "green"}
    # Function for the quiz. Here, a fruit will be chosen randomly
    def quiz(self):
        while True:
            fruit, colour = random.choice(list(self.fruits.items()))
            print("What is the colour of {}".format(fruit), "?")
            user_input = input()
            if user_input.lower() == colour:
                print("That's the correct answer!")
            else:
                print("That's not the correct answer...")
            option = int(input("Enter 0 if you want to play again. Otherwise, enter 1."))
            if option == 1:
                break

print("Welcome to the fruit quiz!")
obj1 = Fruit_quiz()
obj1.quiz()
