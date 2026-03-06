import random

number = random.randint(1,101)
user_input = 0
attempt = 0
while (user_input != number):
    user_input= int(input("Enter your number: "))
    if user_input== number :
        print(f"Congratulations! You guessed the number is {attempt} attempts.")
        attempt+=1
    elif user_input < number:
        print("Enter higher number")
        attempt+=1
    elif user_input > number:
        print("Enter lower number")
        attempt+=1