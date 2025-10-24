import random

def game():
    options = ["rock", "scissor", "paper"]
    user_choice = input("Введіть свій вибір (rock, scissor, paper): ").lower()

    if user_choice not in options:
        print("Невірне значення")
        return

    computer_choice = random.choice(options)
    print(f"Комп’ютер обрав: {computer_choice}")

    if user_choice == computer_choice:
        print("Нічия")
    elif (user_choice == "stone" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Ви перемогли")
    else:
        print("Комп’ютер переміг")

if __name__ == "__main__":
    game()
