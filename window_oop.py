from tkinter import *


class Demo:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry('800x600')
        self.frame.pack()


def main():
    root = Tk()
    app = Demo(root)
    root.title('Demo')
    root.mainloop()


if __name__ == '__main__':
    main()