import tkinter as tk
from tkinter import ttk

def main_window():
    root = tk.Tk()  # makes base window
    title_label = ttk.Label(root, text="New Patient")
    title_label.grid(column=1, row=1, sticky='w')
    mrnlabel = ttk.Label(root, text="Enter patient MRN: ")
    mrnentry = tk.Entry(root)
    mrnentry.grid(column=2, row=3, columnspan=2)
    mrnlabel.grid(column=1, row=3, sticky='w')
    testlabel = ttk.Label(root, text="Choose test: ")
    testlabel.grid(column=1, row= 5, sticky='w')
    root.columnconfigure(0, minsize=30)
    root.columnconfigure(4, minsize=30)
    root.rowconfigure(0, minsize=30)
    root.rowconfigure(2, minsize=30)
    root.rowconfigure(4, minsize=30)
    root.rowconfigure(6, minsize=30)
    root.mainloop() # activate and show window

if __name__ == "__main__":
    main_window()