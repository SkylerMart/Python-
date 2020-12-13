from tkinter import *
import tkinter as tk



class webWindow(Frame):
        def __init__(self, master, *args, **kwargs):
                Frame.__init__(self, master, *args, *kwargs)

                self.master = master
                self.master.minsize(500, 300)
                self.master.maxsize(100, 600)

                self.master.title("Edit html web page")
                self.master.config(bg = "#f0f0f0")
                
                self.webUpdate = StringVar()
                self.webUpdate.set("New savings comming your way!")
                
                self.Webpage_lbl = tk.Label(self.master, text = "Enter Webpage Update: ", bg = "#f0f0f0")
                self.Webpage_lbl.grid(row = 2, column = 0, padx =(10, 0), pady =(10, 0), sticky = NW)
                self.Webpage_txt = tk.Entry(self.master, text = self.webUpdate, bg = 'lightblue', width = 50)
                self.Webpage_txt.grid(row = 2, column =1, rowspan = 5, columnspan = 3, padx =(10, 0), pady =(10, 0), sticky = NW)
                
                self.btn_update = tk.Button(self.master, width = 20, height = 2, bg='lightblue', text = "Update Webpage", command = lambda: self.onUpdate())
                self.btn_update.grid(row = 8, column =2, padx = (15, 0), pady = (45, 10), sticky = SE)
                
        def onUpdate(self):
                file = open("webpggen.html", "w")
                file.write(self.webUpdate.get())
                file.close()





















if __name__ == "__main__":
        root = tk.Tk()
        App = webWindow(root)
        root.mainloop()
