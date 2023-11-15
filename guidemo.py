import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog

def main_window():

    def swap_colors():
        current_color = label.cget("foreground")
        if current_color.string == "red":
            label.configure(foreground="black")
        else:
            label.configure(foreground="red")
        root.after(1000, swap_colors)

    def button_cmd():
        messagebox.askyesno("Verification of Action",
                            "Are you sure you want blinking letters?")
        filename = filedialog.askopenfilename()
        if filename == "":   # canceled
            return
        label.configure(foreground="red")
        root.after(1000, swap_colors)


    root = tk.Tk()
    root.title("GUI Demo")

    label = ttk.Label(root, text="Welcome", font=("Arial", 24))
    label.grid(column=0, row=0)

    button = ttk.Button(root, text="Ok", command=button_cmd)
    button.grid(column=0, row=1)

    root.mainloop()


if __name__ == "__main__":
    main_window()