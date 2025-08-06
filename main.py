from input import get_numbers
from calculator import add_numbers

while True:
    num1, num2 = get_numbers()
    add_numbers(num1, num2)

    choice = input("Do you want to add more numbers? (yes/no): ").strip().lower()
    if choice == "no":
        print("Goodbye!")
        break
