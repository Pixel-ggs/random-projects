# satisfying AF, I hate TK tho :(

import tkinter as tk, random as r, time as t

root = tk.Tk()
root.geometry("300x200")

R = r.randint(0, 225)
G = r.randint(0, 225)
B = r.randint(0, 225)

def rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def gen():
    R = r.randint(0, 225)
    G = r.randint(0, 225)
    B = r.randint(0, 225)
    box.config(bg=rgb(R, G, B))
    t.config(text=f"RGB Values: {R} ; {G} ; {B}")

b = tk.Button(root, text="Generate", command=gen)
b.pack(padx=20, pady=20)

box = tk.Frame(root, width=60, height=40, bg=rgb(R, G, B))
box.pack(padx=20, pady=20)

t = tk.Label(root, text=f"RGB Values: {R} ; {G} ; {B}")
t.pack()

root.mainloop()
