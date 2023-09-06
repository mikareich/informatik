from tkinter import *
import serial


class Serial:
    def __init__(self, port):
        print("init")
        # self.s = serial.Serial(port)
        # self.s.setRTS(False)

    def __del__(self):
        print("del")
        # self.s.close()

    def rtsOn(self, event):
        print("rtsOn")
        # self.s.setRTS(True)

    def rtsOff(self, event):
        print("rtsOff")
        # self.s.setRTS(False)

    def getCts(self):
        print("getCts")
        return True
        # return self.s.getCTS()


class App(Tk):
    def __init__(self, serial):
        Tk.__init__(self)
        self.serial = serial

        # Window settings
        self.title("RTS und CTS")
        self.geometry("300x100+100+200")

        # RTS Button
        button = Button(master=self, text="RTS an/aus")
        button.bind("<Button-1>", self.serial.rtsOn)
        button.bind("<ButtonRelease>", self.serial.rtsOff)
        button.place(x=70, y=35)

        # CTS Led
        self.canvas = Canvas(master=self, width=60, height=60)
        self.canvas.place(x=170, y=20)
        item = self.canvas.create_oval(10, 10, 50, 50, fill="#550000")
        self.canvas.itemconfig(item, tags=("LED"))

        # Call checkCts and start mainloop
        self.checkCts()
        self.mainloop()

    def checkCts(self):
        if self.serial.getCts():
            self.canvas.itemconfig("LED", fill="#ff0000")
        else:
            self.canvas.itemconfig("LED", fill="#550000")

        self.after(100, self.checkCts)


serial = Serial("COM3")
view = App(serial)
