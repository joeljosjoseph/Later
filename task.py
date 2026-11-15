from datetime import datetime, timedelta
import random

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
