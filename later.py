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
        # return something like: "Write essay (due 2026-11-20 17:00, delayed 0 times)"
        return "Write an essay: due " + self.deadline.strftime("%Y-%m-%d %H:%M")
        # pass

t = Task("Write essay", datetime.now() + timedelta(days=3))
print(t)
print(t.hours_left())