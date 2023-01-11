import tkinter as tk
import json
import random

# Funzione per la finestra "SI"
def on_yes():
    # Crea una nuova finestra
    window = tk.Toplevel(root)
    window.title("Finestra SI")
    
    # Testo al centro
    tk.Label(window, text="Inserisci il numero di valori da selezionare:").pack()
    
    # Casella di testo
    e = tk.Entry(window)
    e.pack()
    
    # Bottone "Vai"
    def on_go():
        # Legge il valore inserito nella casella di testo
        n = int(e.get())
        # Apri il file JSON
        with open("insulti.json") as f:
            data = json.load(f)
        # Seleziona n valori casuali
        values = random.choice(data, n)
        # Crea una nuova finestra per visualizzare i valori selezionati
        new_window = tk.Toplevel(window)
        new_window.title("Valori selezionati")
        tk.Label(new_window, text="Valori selezionati:").pack()
        # Barra scorrevole per scorrere i valori
        scrollbar = tk.Scrollbar(new_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # Listbox per visualizzare i valori
        lb = tk.Listbox(new_window, yscrollcommand=scrollbar.set)
        for value in values:
            lb.insert(tk.END, value)
        lb.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=lb.yview)
    tk.Button(window, text="Vai", command=on_go).pack()
    
# Funzione per la finestra "NO"
def on_no():
    root.destroy()

# Crea la finestra principale
root = tk.Tk()
root.title("Interfaccia grafica")

# Testo in alto al centro
tk.Label(root, text="Vuoi continuare?", font=("Helvetica", 16)).pack()

# Testo al centro
tk.Label(root, text="Premi SI per continuare o NO per uscire").pack()

# Bottone "SI"
tk.Button(root, text="SI", command=on_yes).pack()

# Bottone "NO"
tk.Button(root, text="NO", command=on_no).pack()

# Avvia il ciclo di eventi Tkinter
root.mainloop()
