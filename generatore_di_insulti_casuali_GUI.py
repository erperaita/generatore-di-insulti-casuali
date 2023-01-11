import tkinter as tk
import time

root = tk.Tk()
root.geometry("400x300")

label_top = tk.Label(root, text="Testo in alto al centro", font=("Arial", 16), anchor="center")
label_top.place(relx=0.5, rely=0.1, anchor="center")

label_center = tk.Label(root, text="Testo al centro", font=("Arial", 14), anchor="center")
label_center.place(relx=0.5, rely=0.5, anchor="center")

def on_yes_click():
    new_root = tk.Tk()
    new_root.geometry("400x300")

    back_button = tk.Button(new_root, text="Torna Indietro", font=("Arial", 12), command=new_root.destroy)
    back_button.place(relx=0.8, rely=0.8)

    new_label = tk.Label(new_root, text="Testo Nuova Finestra", font=("Arial", 14), anchor="center")
    new_label.place(relx=0.5, rely=0.5, anchor="center")

    new_entry = tk.Entry(new_root, width=20)
    new_entry.place(relx=0.5, rely=0.7, anchor="center")
    new_root.mainloop()

def on_no_click():
    goodbye_label = tk.Label(root, text="Arrivederci!", font=("Arial", 14), anchor="center")
    goodbye_label.place(relx=0.5, rely=0.5, anchor="center")
    root.update()
    time.sleep(5)
    root.destroy()
    sys.exit()

button_yes = tk.Button(root, text="Si", font=("Arial", 12), bg="green", command=on_yes_click)
button_yes.place(relx=0.2, rely=0.8)

button_no = tk.Button(root, text="No", font=("Arial", 12), bg="red", command=on_no_click)
button_no.place(relx=0.8, rely=0.8)

root.mainloop()
