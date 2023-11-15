import tkinter as tk
from tkinter import ttk

def main_window():
    root = tk.Tk()  # makes base window
    title_label = ttk.Label(root, text="New Patient")
    title_label.grid(column=1, row=1, sticky='w')
    mrnlabel = ttk.Label(root, text="Enter patient MRN: ")
    mrnentry = tk.Entry(root)
    mrnentry.grid(column=3, row=3, columnspan=2)
    mrnlabel.grid(column=1, row=3, sticky='w')
    testlabel = ttk.Label(root, text="Choose test: ")
    testlabel.grid(column=1, row= 5, sticky='w')
    for i in [0,2,5]:
        root.columnconfigure(i, minsize=30)
    for i in [0,2,4,6]:
        root.rowconfigure(i, minsize=30)

    root.mainloop() # activate and show window

if __name__ == "__main__":
    main_window()