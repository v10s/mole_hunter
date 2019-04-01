import tkinter as tk


root = tk.Tk()
hi = tk.StringVar()
hi.set("234")
label1 = tk.Label(root,text="SCORE")
value1 = tk.Label(root,textvariable=hi)

label1.pack()
value1.pack()




root.mainloop()
