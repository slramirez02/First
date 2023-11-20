import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk


def tk_img_from_filename(filename):
    pil_img = Image.open(filename)
    size = pil_img.size
    pil_img = pil_img.resize((150,150))
    tk_image = ImageTk.PhotoImage(pil_img)
    return tk_image


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

    tk_img = tk_img_from_filename("Images/img.png")
    image_label = ttk.Label(root, image=tk_img)
    image_label.grid(column=0, row=2)

    root.mainloop()


if __name__ == "__main__":
    main_window()