from datetime import datetime, timedelta
import random
import json

SAVE_FILE = "tasks.json"

SUGGESTIONS = [
    "Reorganize your desktop icons first. It's basically prep work.",
    "Make coffee. Great work starts with hydration.",
    "Watch one productivity video. Knowledge is progress.",
    "Clean your keyboard. You can't work in these conditions.",
    "Check your emails. Someone might need you urgently.",
    "Create a to-do list for your to-do list.",
    "Adjust your chair. Ergonomics are important.",
    "Find the perfect playlist. Music fuels productivity.",
    "Take a quick break. Mental preparation is essential.",
    "Research the best way to get started. Preparation is everything.",
    "Open 15 browser tabs. You're building momentum.",
    "Check the weather. You need the right atmosphere."
]

EXCUSE_STARTS = [
    "I would have started, but",
    "Honestly, I was about to, but",
    "I had everything planned, except",
    "My productivity was interrupted because",
    "I was mentally prepared, but",
    "I swear I was going to, but",
    "It's not procrastination if",
    "I can't possibly work until"
]

EXCUSE_REASONS = [
    "my ex texted me.",
    "my chair was at a bad angle.",
    "my coffee wasn't emotionally ready.",
    "the Wi-Fi looked suspicious.",
    "I haven't found the perfect playlist.",
    "my keyboard needs emotional support.",
    "the universe clearly needs me to rest.",
    "I accidentally opened YouTube.",
    "my brain is still loading.",
    "it's an odd-numbered minute.",
    "I need to mentally prepare for mentally preparing.",
    "my desk has the wrong energy.",
    "I forgot what I was supposed to do.",
    "I work better under pressure, and there's no pressure yet."
]

DELAY_REASONS = [
    "Research shows your brain peaks later today.",
    "Starting now would be rushing. Quality takes patience.",
    "You're not procrastinating; you're building anticipation.",
    "The deadline isn't close enough to activate your full potential.",
    "Great ideas need time to marinate.",
    "Your future self is better equipped to handle this.",
    "It's important to respect your current lack of motivation.",
    "You should wait for the perfect moment. It builds character.",
    "Your productivity window is probably tomorrow morning.",
    "A little more planning will definitely make starting easier.",
    "You're giving your brain time to develop a strategy.",
    "The task isn't going anywhere. Unfortunately."
]

def get_suggestion():
    return random.choice(SUGGESTIONS)

def get_excuse():
    return f"{random.choice(EXCUSE_STARTS)} {random.choice(EXCUSE_REASONS)}"

def get_delay_reason():
    return f"{random.choice(DELAY_REASONS)}"
class Task:
    def __init__(self, name, deadline):

        self.name = name
        self.deadline = deadline
        self.start_time = datetime.now()   # when you "plan" to start
        self.times_delayed = 0             
        # pass

    def task_name(self):
        return self.name

    def hours_left(self):

        time_left = (self.deadline - datetime.now()).total_seconds() / 3600
        time_left = round(time_left, 2)

        return int(time_left) if time_left.is_integer() else time_left

    def delay(self):

        delay = random.choice([15, 30, 60, 120])
        self.start_time = self.start_time + timedelta(minutes=delay)
        self.times_delayed += 1

        return self.time_left_text()

    def get_delayed_times(self):

        return self.times_delayed

    def time_left_text(self):

        h = self.hours_left()

        if h < 0:
            return "overdue"
        if h < 1:
            return f"{int(h * 60)} minutes"
        
        return f"{h:g} hours"

    def panic_level(self):

        h = self.hours_left()

        if h < 0:
            return "You're cooked💀"
        elif h < 1:
            return "Get off yo ass and get to it" 
        elif h < 6:
            return "Heyy don't you slack off now!"
        elif h < 24:
            return "Sip on your coffee and start doing it"
        elif h < 72:
            return "Are you tired? If not lets work on it a little"
        else:
            return "Relax and enjoy that beer🌴"

    def panic_bar(self):

        h = max(self.hours_left(), 0)

        # 0 hours left = full bar, 72+ hours left = empty bar
        filled = int(10 * (1 - min(h, 72) / 72))

        return "[" + "#" * filled + "-" * (10 - filled) + "]"

    def to_dict(self):
        return {
            "name": self.name,
            "deadline": self.deadline.isoformat(),
            "start_time": self.start_time.isoformat(),
            "times_delayed": self.get_delayed_times(),
        }

    def is_panic(self):
            return 0 < self.hours_left() < 1

    @staticmethod
    def from_dict(d):
        t = Task(d["name"], datetime.fromisoformat(d["deadline"]))
        t.start_time = datetime.fromisoformat(d["start_time"])
        t.times_delayed = d["times_delayed"]
        return t

    def __str__(self):
        return f"{self.name} due at {self.deadline.strftime("%Y-%m-%d %H:%M")}"




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
    save_tasks()

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
        save_tasks()

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
        save_tasks()

    except ValueError:
        print("Thats not a number bro!?")

def save_tasks():
    with open(SAVE_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)

def load_tasks():
    try:
        with open(SAVE_FILE) as f:
            for d in json.load(f):
                tasks.append(Task.from_dict(d))
    except FileNotFoundError:
        pass   # first run: no file yet, that's fine

def main():
    load_tasks()
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