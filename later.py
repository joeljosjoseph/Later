from datetime import datetime, timedelta

class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        pass

    def hours_left(self):
        time_left = (self.deadline - datetime.now()).total_seconds() / 3600
        return time_left

    def __str__(self):
        return f"{self.name} due at {self.deadline.strftime("%Y-%m-%d %H:%M")}"

# t = Task("Write essay", datetime.now() + timedelta(days=3))
# print(t)
# print(t.hours_left())

tasks = []   # list holds all the tasks

# ask for the task name, deadline, then build a Task and append it to tasks
def add_task():
    name = input("Task name: ").strip()
    try:
        deadline = float(input("Due in how many hours? "))
    except ValueError:
        print("That's not a number. Procrastinating already?")
        return
    
    t = Task(name, datetime.now() + timedelta(hours=deadline))
    tasks.append(t)

def list_tasks():
    # tasks is empty check
    if len(tasks) == 0:
        print("No tasks. Suspiciously productive of you.")
    else:
        #loop through tasks
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

def main():
    while True:
        print("\n1) Add task  2) List tasks  3) Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            print("Leaving already? Bold of you to assume it's done.")
            break
        else:
            print("Invalid choice")

main()