# Task 1 To do list
choice = 'random'
task_list = list()

def displayMenu():
    print("Menu: ")
    print("a. Add an item: ")
    print("b. Mark as done: ")
    print("c. View items: ")
    print("d. Exit: ")

while choice != 'd':
    displayMenu()
    choice = input("Enter your choice: ")

    if choice == 'a':
        task = input("What is to be added? ")
        task_list.append(task)
        print("Added item: ", task)
    elif choice == 'b':
        task = input("What is to be deleted? ")
        if task in task_list:
            task_list.remove(task)
            print("Removed item:", task)
        else:
            print("Item does not exist in the task list")
    elif choice == 'c':
        if len(task_list) == 0:
            print("There are no items in the task list.")
        else:
            print("List of task items: ")
            for task in task_list:
                print(task)
    elif choice == 'd':
        print("Goodbye")