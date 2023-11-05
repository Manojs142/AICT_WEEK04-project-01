def start_game():
    print("Welcome to the Text Adventure Game!")
    first_decision()
def first_decision():
    print("\nYou find yourself at a crossroads. Do you want to go left or right?")
    choice = input("Type 'left' or 'right': ").lower()
    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        first_decision()
def left_path():
    print("\nYou chose the left path. You encounter a wild animal.")
def right_path():
    print("\nYou chose the right path. You find a treasure chest.")
start_game()