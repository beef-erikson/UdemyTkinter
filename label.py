import tkinter

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('Hello!!!')
    root.geometry('300x300')

    # Long way
    var1 = tkinter.StringVar()
    var2 = tkinter.StringVar()

    label1 = tkinter.Label(root, textvariable=var1)
    label2 = tkinter.Label(root, textvariable=var2)

    var1.set('Hello World!')
    label1.pack()
    var2.set('In the middle\nis another line')
    label2.pack(expand=tkinter.TRUE)

    # Short way
    label3 = tkinter.Label(root, text='Hello again', fg='red', bg='black')
    label3.pack(expand=tkinter.TRUE)
    root.mainloop()
