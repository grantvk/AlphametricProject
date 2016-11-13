from tkinter import *
from tkinter import ttk


# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
#     except ValueError:
#         pass
def solve(*args):
    try:
        value = float(topWord.get())
        solution.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


root = Tk()
root.title("Alphametric Solver")
#root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()
topWord = StringVar()
botWord = StringVar()
answer = StringVar()
solution = StringVar()

topWord_entry = ttk.Entry(mainframe, width=7, textvariable=topWord)
topWord_entry.grid(column=2, row=2, sticky=(W, E))
botWord_entry = ttk.Entry(mainframe, width=7, textvariable=botWord)
botWord_entry.grid(column=2, row=3, sticky=(W, E))
answer_entry = ttk.Entry(mainframe, width=7, textvariable=answer)
answer_entry.grid(column=2, row=5, sticky=(W, E))

#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Solve", command=solve).grid(column=3, row=7, sticky=W)
ttk.Label(mainframe, textvariable=solution).grid(column=2, row=6, sticky=(W, E))

ttk.Label(mainframe, text="Insert a two Word Alphametric Problem!").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="Top Word").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="+").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="Bottom Word").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text ="___________________________________________").grid(column=2, row=4, sticky=(W,E))
ttk.Label(mainframe, text="Sum").grid(column=3, row=5, sticky=W)
ttk.Label(mainframe, text="Solution").grid(column=3, row=6, sticky=W)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
# ttk.Label(mainframe, text="top").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

topWord_entry.focus()
root.bind('<Return>', solve)

root.mainloop()