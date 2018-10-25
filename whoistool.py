from Tkinter import *
import socket, sys
from PIL import Image, ImageTk
import tkMessageBox

root = Tk()
root.title("Whois Tool")
root.resizable(0, 0)

frame = Frame(root)

text = Text()
text1 = Text()

image = Image.open("/home/c0deninja/Pictures/hacker.jpg")
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.pack()


text1.config(width=15, height=1)
text1.pack()

def version():
    tkMessageBox.showinfo("Version", "Whois tool by c0deninja")

def button1():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("com.whois-servers.net", 43))
        s.send(text1.get("1.0", END) + "\r\n")
        response = ''
        while True:
            a = s.recv(4096)
            response += a
            if a == '':
                break
        s.close()
        text.insert(END, response)

def clear():
        text.delete("1.0", END)

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="version", command=version)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

b = Button(root, text="Enter", width=10, height=2, command=button1)
b.pack()

c = Button(root, text="Clear", width=10, height=2, command=clear)
c.pack()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text.config(width=60, height=15)
text.pack(side=LEFT, fill=Y)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)


root.mainloop()
