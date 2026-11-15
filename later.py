from datetime import datetime, timedelta
from content import get_excuse, get_suggestion, get_delay_reason
from storage import save_tasks, load_tasks
from task import Task
import random

tasks = []   # list holds all the tasks

# ask for the task name, deadline, then build a Task and append it to tasks
def add_task():
    name = input("What task? ").strip()

    try:
        deadline = float(input("Due in how many hours? "))

    except ValueError:
        print("That's not a number. Procrastinating already?")
        return
    
    t = Task(name, datetime.now() + timedelta(hours=deadline))
    tasks.append(t)
    save_tasks(tasks)

def start_task():

    if(len(tasks) == 0):
        print("Zero tasks available? Did you even add any?!")
        print("Let's try that again")
        return

    list_tasks(True)

    try:
        task_num = int(input("So which task we working on? "))

        if task_num < 1 or task_num > len(tasks):
            print("Not even a task on the list. Time to lay off of the shrooms.")
            return

        t = tasks[task_num - 1]

        if t.is_panic():
            print(f"You have {t.time_left_text()} to complete it and you want to DELAY it?")
            print("Do you wanna be a failure or a success? GET TO WORK!!!")
            return
        t.delay()

        print(
            f"Guess what?! You get more time to relax since "
            f"{t.start_time.strftime('%H:%M')} is a better time to start."
        )
        print(get_delay_reason())
        save_tasks(tasks)

    except ValueError:
        print("Thats not a number bro!?")
        return

def check_panic_tasks():
    for t in tasks:
        if t.is_panic():
            print(f"🚨 '{t.name}' is due in {t.time_left_text()}. Why are you here?")
        elif t.hours_left() < 0:
            print(f"💀 '{t.name}' is overdue. You done done fr!")
    

def list_tasks(tasksOnly = False):
    # tasks is empty check
    if len(tasks) == 0:
        print("No tasks. Suspiciously productive of you.")

    else:
        #loop through tasks
        for i, t in enumerate(tasks, start=1):
            extra_info = ""

            if not tasksOnly:
                extra_info = (
                    f"Start: {t.start_time.strftime('%H:%M')} "
                    f"(delayed {t.get_delayed_times()}x) "
                    f"{t.panic_bar()} {t.panic_level()}"
                )

            print(f"{i}. {t.task_name()} is due in {t.time_left_text()}. {extra_info}")

def complete_task():
    if not tasks:
        print("Zero tasks available? Did you even add any?!")
        print("Let's try that again.")
        return

    list_tasks(True)

    try:
        task_num = int(input("So which task did you complete lmao? "))

        if task_num < 1 or task_num > len(tasks):
            print("Not even a task on the list. Time to lay off of the shrooms.")
            return

        t = tasks.pop(task_num - 1)

        print("Wait what. You COMPLETED A TASK?!!!")

        tries = t.get_delayed_times()

        if tries >= 5:
            delayed_message = (
                f"And it took you {tries} tries to complete it...."
                "it's a wonder you even finished it at all."
            )
        elif tries >= 2:
            delayed_message = (
                f"And you delayed it {tries} times. "
                "Not bad for a professional procrastinator."
            )
        else:
            delayed_message = (
                f"And you only delayed it {tries} times? "
                "You're a fake procrastinator. You should be ashamed of yourself."
            )

        print(delayed_message)
        save_tasks(tasks)

    except ValueError:
        print("Thats not a number bro!?")


def main():
    load_tasks(tasks)
    check_panic_tasks()

    while True:
        print("\n1) Add task 2) Start Task 3) List tasks 4) Complete Task 5) Get a suggestion 6) Generate Excuse 7) Quit")
        choice = input("Whats the plan? ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            start_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            print(get_suggestion())
        elif choice == "6":
            print(get_excuse())
        elif choice == "7":
            print("Leaving already? Its alright. As long there's a tomorrow right? Right.")
            break
        else:
            print("Invalid choice")

main()