from PIL import ImageTk, Image
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

mainwindow = tk.Tk()
# help(tk.Tk().configure)
mainwindow.title("INFO LEAK APP")
mainwindow.geometry('826x720')
mainwindow.configure(background="lightblue", highlightbackground="lime")
mainwindow.columnconfigure(0, weight=1)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=1)
mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=1)
mainwindow.rowconfigure(2, weight=1)
strtframe = tk.Frame(mainwindow, borderwidth=5, relief="raised", width=600, height=600)
strtframe.columnconfigure(0, weight=1)
strtframe.columnconfigure(1, weight=1)
strtframe.columnconfigure(2, weight=1)
strtframe.rowconfigure(0, weight=1)
strtframe.rowconfigure(1, weight=1)
strtframe.rowconfigure(2, weight=1)
strtframe.grid(row=0, column=0, columnspan=3, rowspan=3)
pth = r"C:\Users\gaikw\Downloads\_554b6762-1b58-43dd-a4e7-a8a862273da2.jpeg"
myimg = ImageTk.PhotoImage(Image.open(pth).resize((600, 600)))
lbl1 = tk.Label(strtframe, anchor="center", image=myimg)
lbl1.columnconfigure(0, weight=1)
lbl1.columnconfigure(1, weight=1)
lbl1.columnconfigure(2, weight=1)
lbl1.rowconfigure(0, weight=1)
lbl1.rowconfigure(1, weight=1)
lbl1.rowconfigure(2, weight=1)
lbl1.grid()
# # lbl1['image'] = myimg
button1 = tk.Button(mainwindow, text="Lets Start!", bg="LemonChiffon", anchor="center")
button1.grid(row=2, column=1, sticky="ew")
mainwindow.mainloop()
