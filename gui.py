import tkinter as tk
from tkinter import ttk

def main_window():
    root = tk.Tk()  # makes base window
    title_label = ttk.Label(root, text="My GUI")
    label2 = ttk.Label(root, text="Other")
    title_label.grid(column=0, row=1)
    label2.grid(column=1, row=2)
    root.mainloop() # activate and show window

if __name__ == "__main__":
    main_window()
    

