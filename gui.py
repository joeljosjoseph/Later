import tkinter as tk
from tkinter import messagebox
from later import tasks, load_tasks, save_tasks, get_excuse

load_tasks(tasks)

root = tk.Tk()
root.title("Later™")
root.geometry("520x400")

listbox = tk.Listbox(root, font=("Consolas", 11))
listbox.pack(fill="both", expand=True, padx=10, pady=10)

def refresh():
    listbox.delete(0, tk.END)
    for t in tasks:
        listbox.insert(tk.END, f"{t.name} | due in {t.time_left_text()} | {t.panic_level()}")

def on_excuse():
    messagebox.showinfo("Your excuse", get_excuse())

btn_frame = tk.Frame(root)
btn_frame.pack(pady=(0, 10))
tk.Button(btn_frame, text="Excuse", command=on_excuse).pack(side="left", padx=5)

refresh()
root.mainloop()