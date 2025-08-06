def get_marks():
    while True:
        try:
            marks = int(input("Enter your marks (0 - 100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100. Please try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def assign_grade(marks):
    if 75 <= marks <= 100:
        return "A"
    elif 65 <= marks <= 74:
        return "B"
    elif 55 <= marks <= 64:
        return "C"
    elif 35 <= marks <= 54:
        return "S"
    else:
        return "F"

def main():
    marks = get_marks()
    grade = assign_grade(marks)
    print(f"✅ Your grade is: {grade}")

if __name__ == "__main__":
    main()
