class ToDoList:
    def __init__(self):
        self.to_do_list = []

    def add_task(self, task):
        self.to_do_list.append(task)
        print(f'Task "{task}" added.')

    def update_task(self, task_no, updated_task):
        if task_no <= len(self.to_do_list):
            self.to_do_list[task_no - 1] = updated_task
            print(f'Task {task_no} updated to "{updated_task}".')
        else:
            print("This task does not exist.")

    def view_tasks(self):
        print("To-Do List:")
        for i, task in enumerate(self.to_do_list):
            print(f"{i+1}. {task}")

    def delete_task(self, task_no):
        if task_no <= len(self.to_do_list):
            print(f'Task "{self.to_do_list[task_no-1]}" deleted.')
            del self.to_do_list[task_no - 1]
        else:
            print("Task does not exist.")


if __name__ == "__main__":
    to_do_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Update task")
        print("3. View tasks")
        print("4. Delete task")
        print("5. Exit")

        option = int(input("\nChoose an option: "))

        if option == 1:
            task = input("Enter task: ")
            to_do_list.add_task(task)

        elif option == 2:
            task_no = int(input("Enter task number to update: "))
            updated_task = input("Enter updated task: ")
            to_do_list.update_task(task_no, updated_task)

        elif option == 3:
            to_do_list.view_tasks()

        elif option == 4:
            task_no = int(input("Enter task number to delete: "))
            to_do_list.delete_task(task_no)

        elif option == 5:
            print("Exiting...")
            break

        else:
            print("Invalid option. Please select again.")
