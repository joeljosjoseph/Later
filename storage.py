import json
from task import Task
from pathlib import Path

SAVE_FILE = Path.home() / ".later_tasks.json"

def save_tasks(tasks):
    with open(SAVE_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)

def load_tasks(tasks):
    try:
        with open(SAVE_FILE) as f:
            for d in json.load(f):
                tasks.append(Task.from_dict(d))
    except FileNotFoundError:
        pass   # first run: no file yet, that's fine
