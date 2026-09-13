def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print(f"{value} is not a valid number. Please try again.")


def show_menu():
    print("\nChoose a tool:")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Countdown Timer")
    print("4. Quit")


# Tool 1: calculate with two numbers and a selected operation.
def simple_calculator():
    print("\nSimple Calculator")
    first = get_number("First number: ")
    operation = input("Operation (+, -, *, /): ").strip()
    second = get_number("Second number: ")

    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    elif operation == "/":
        if second == 0:
            print("Division by zero is not allowed.")
            return
        result = first / second
    else:
        print(f"{operation} is not a supported operation.")
        return

    print(f"{first:g} {operation} {second:g} = {result:g}")


# Tool 2: manage a list that changes as tasks are added and removed.
def todo_list():
    tasks = []
    print("\nTo-Do List")
    while True:
        action = input("Choose add, remove, show, or done: ").strip().lower()
        if action == "add":
            task = input("Task to add: ").strip()
            if task:
                tasks.append(task)
                print(f"Added task: {task}")
            else:
                print("A task cannot be empty.")
        elif action == "remove":
            task = input("Task to remove: ").strip()
            if task in tasks:
                tasks.remove(task)
                print(f"Removed task: {task}")
            else:
                print(f"I could not find {task} in your list.")
        elif action == "show":
            if tasks:
                print("Your tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            else:
                print("Your task list is empty.")
        elif action == "done":
            print("Leaving the to-do list.")
            return
        else:
            print(f"{action} is not a to-do list command.")


# Tool 3: use a loop to count down from the user's number to zero.
def countdown_timer():
    print("\nCountdown Timer")
    start = get_number("Count down from: ")
    if start < 0 or not start.is_integer():
        print("Please enter a non-negative whole number.")
        return
    start = int(start)
    for number in range(start, -1, -1):
        print(f"Countdown: {number}")
    print("Countdown complete!")


print("Welcome to the Handy Python Toolkit!")
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        simple_calculator()
    elif choice == "2":
        todo_list()
    elif choice == "3":
        countdown_timer()
    elif choice == "4":
        print("Thanks for using the Handy Python Toolkit. Goodbye!")
        break
    else:
        print("I do not recognize that choice. Please enter 1, 2, 3, or 4.")
