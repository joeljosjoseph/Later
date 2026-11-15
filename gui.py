import tkinter as tk
from tkinter import messagebox
from storage import load_tasks, save_tasks
from content import get_excuse, get_suggestion, get_delay_reason, get_completion_message
from task import Task
from datetime import datetime, timedelta

tasks = []

load_tasks(tasks)

root = tk.Tk()
root.title("Later™")
root.geometry("600x400")

listbox = tk.Listbox(root, font=("Consolas", 11), exportselection=False)
listbox.pack(fill="both", expand=True, padx=10, pady=10)

def refresh():
    sel = listbox.curselection()
    listbox.delete(0, tk.END)
    for i, t in enumerate(tasks):
        listbox.insert(tk.END, f"{t.name} | due in {t.time_left_text()} | {t.panic_level()}")
        if t.is_panic():
            listbox.itemconfig(i, bg="#ffcccc", fg="#a00000")    # red row in panic mode
        elif t.hours_left() < 0:
            listbox.itemconfig(i, bg="#555555", fg="white")      # overdue = grey
    for i in sel:
        listbox.selection_set(i)

def tick():
    refresh()
    root.after(1000, tick) 

def on_excuse():
    messagebox.showinfo("Your excuse", get_excuse())


form = tk.Frame(root)
form.pack(pady=(0, 5))

tk.Label(form, text="Task:").pack(side="left")
name_entry = tk.Entry(form, width=20)
name_entry.pack(side="left", padx=5)

tk.Label(form, text="Due in (hours):").pack(side="left")
hours_entry = tk.Entry(form, width=6)
hours_entry.pack(side="left", padx=5)

def on_add():
    name = name_entry.get().strip()
    if not name:
        messagebox.showerror("Oops", "Task needs a name.")
        return
    try:
        hours = float(hours_entry.get())
    except ValueError:
        messagebox.showerror("Oops", "Hours must be a number. Procrastinating already?")
        return
    tasks.append(Task(name, datetime.now() + timedelta(hours=hours)))
    save_tasks(tasks)
    name_entry.delete(0, tk.END)    # clear the boxes
    hours_entry.delete(0, tk.END)
    refresh()

def selected_task():
    sel = listbox.curselection()
    if not sel:
        messagebox.showinfo("Hmm", "Click a task first.")
        return None
    return tasks[sel[0]]

def on_start():
    t = selected_task()
    if t is None:
        return
    if t.is_panic():
        messagebox.showwarning(
            "NOPE",
            f"You have {t.time_left_text()} to complete it and you want to DELAY it?\n"
            "GET TO WORK!!!")
        return
    t.delay()
    save_tasks(tasks)
    messagebox.showinfo(
        "Good news!",
        f"You get more time to relax. {t.start_time.strftime('%H:%M')} "
        f"is a better time to start.\n\n{(get_delay_reason())}")
    refresh()

def on_done():
    t = selected_task()
    if t is None:
        return
    tries = t.get_delayed_times()
    tasks.remove(t)
    save_tasks(tasks)
    messagebox.showinfo(
        "Wait what.",
        f"You COMPLETED A TASK?!!!\n\n{get_completion_message(tries)}")
    refresh()

def on_suggestion():
    messagebox.showinfo("Productive procrastination", get_suggestion())

btn_frame = tk.Frame(root)
btn_frame.pack(pady=(0, 10))

tk.Button(btn_frame, text="Add", command=on_add).pack(side="left", padx=5)
tk.Button(btn_frame, text="Start", command=on_start).pack(side="left", padx=5)
tk.Button(btn_frame, text="Complete", command=on_done).pack(side="left", padx=5)
tk.Button(btn_frame, text="Suggestion", command=on_suggestion).pack(side="left", padx=5)
tk.Button(btn_frame, text="Excuse", command=on_excuse).pack(side="left", padx=5)

tick()
root.mainloop()