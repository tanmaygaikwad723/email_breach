from PIL import ImageTk, Image
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

inp_tex = ("Caution...!!!, The result of the search is coming from an api which may or may not have limited data,"
           "if your email is not found in any data breach then the creator of this project does not gaurantee that your email"
           "/credentials wasn't leaked at all but you can have a sense of relief that it wasn't leaked in some"
           " data breaches...!")
class mainapp():
    def __init__(self):
        self.mainwindow = tk.Tk()
        self._frame = startpage(self.mainwindow)
        self.mainwindow.title("INFO LEAK APP")
        self.mainwindow.geometry('826x720')
        self.mainwindow.configure(background="#026d74", highlightbackground="lime")
        self.mainwindow.columnconfigure(0, weight=1)
        self.mainwindow.columnconfigure(1, weight=1)
        self.mainwindow.columnconfigure(2, weight=1)
        self.mainwindow.rowconfigure(0, weight=1)
        self.mainwindow.rowconfigure(1, weight=1)
        self.mainwindow.rowconfigure(2, weight=1)
        self.button1 = tk.Button(self.mainwindow, text="Lets Start!", bg="LemonChiffon", anchor="center", command=self.switch_frm)
        self.button1.grid(row=2, column=1, sticky="ew")
        self.btn = tk.Button(self.mainwindow, text="exit..!", bg="red", anchor="center")
        self.btn.grid(row=2, column=2)

    def switch_frm(self):
        if self._frame is not None:
            self._frame.frame.destroy()
            self.button1.destroy()
            self.btn.destroy()
            self._frame.lbl.destroy()
        newframe = entrypage(self.mainwindow)
        self._frame = newframe


class startpage():
    def __init__(self, master):
        self.frame = tk.Frame(master, borderwidth=5, relief="sunken", width=600, height=600, background="#04e6bf")
        # self.frame = tk.Frame(master, borderwidth=5, relief="raised", width=600, height=600)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.grid(row=0, column=0, columnspan=3, rowspan=3)
        pth = r"_554b6762-1b58-43dd-a4e7-a8a862273da2.jpeg"
        self.myimg = ImageTk.PhotoImage(Image.open(pth).resize((600, 600)))
        self.lbl = tk.Label(self.frame, anchor="center", image=self.myimg)
        self.lbl.grid()


class entrypage():
    def __init__(self, master):
        self.frm = tk.Frame(master=master, borderwidth=5, relief="sunken", width=600, height=600, bg="#389ca2", pady=5, padx=5)
        self.frm.columnconfigure(0, weight=1)
        self.frm.columnconfigure(1, weight=1)
        self.frm.columnconfigure(2, weight=1)
        self.frm.rowconfigure(0, weight=1)
        self.frm.rowconfigure(1, weight=1)
        self.frm.rowconfigure(2, weight=1)
        self.frm.grid(row=0, column=0, columnspan=3, rowspan=3)
        self.frm.grid_propagate(False)
        lbl1 = tk.Text(self.frm, width=50, height=self.frm.grid_bbox(0,0)[3], bg="#4ADEDE", fg="red", font=('calibre', 10, 'bold'))
        lbl1.grid(row=0, column=0, columnspan=3, sticky="ns")
        lbl1.insert('1.0', inp_tex)
        lbl2 = tk.Label(self.frm, text="email:", font=('calibre', 10, 'bold'), bg="#389ca2")
        lbl2.grid(row=1, column=0)
        self.ent = tk.StringVar()
        emal = tk.Entry(self.frm, textvariable=self.ent, width=70)
        emal.grid(row=1, column=1, columnspan=3)
        btn2 = tk.Button(master=master, text="submit", fg="red", bg="cyan", font=('calibre', 10, 'bold'))
        btn2.grid(row=3, column=0, sticky="ne")
        btn3 = tk.Button(master, text="Exit!!!", fg="red", bg="cyan", font=('calibre', 10, 'bold'))
        btn3.grid(row=3, column=1, sticky="ne")


if __name__ == "__main__":
    app = mainapp()
    app.mainwindow.mainloop()