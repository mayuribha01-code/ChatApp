import socket
import threading
from tkinter import *

def send(listbox, entry):
    try:
        message = entry.get()

        if message:
            listbox.insert(END, "Client: " + message)
            s.send(message.encode("utf-8"))

        entry.delete(0, END)

    except Exception as e:
        listbox.insert(END, "Error: " + str(e))

def receive(listbox):
    while True:
        try:
            message = s.recv(1024)

            if not message:
                break

            listbox.insert(
                END,
                "Server: " + message.decode("utf-8")
            )

        except:
            break

root = Tk()

entry = Entry()
entry.pack(side=BOTTOM)

listbox=Listbox(root)
listbox.pack()


button = Button(root,text="Send",command=lambda: send(listbox,entry))
button.pack(side=BOTTOM)

root.title('Client')

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 8000
try:
    s.connect((HOST_NAME, PORT))
except Exception as e:
    print("Connection Error:", e)
threading.Thread(
    target=receive,
    args=(listbox,),
    daemon=True
).start()
root.mainloop()
