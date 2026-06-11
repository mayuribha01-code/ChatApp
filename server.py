import socket
import threading
from tkinter import *

def send(listbox, entry):
    try:
        message = entry.get()

        if message:
            listbox.insert(END, "Server: " + message)
            client.send(message.encode("utf-8"))

        entry.delete(0, END)

    except Exception as e:
        listbox.insert(END, "Error: " + str(e))

def receive(listbox):
    while True:
        try:
            message_from_client = client.recv(1024)
            if not message_from_client:
                break

            listbox.insert(
                END,
                "Client: " + message_from_client.decode("utf-8")
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

root.title('Server')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST_NAME = socket.gethostname()
PORT = 8000

try:
    s.bind((HOST_NAME, PORT))
    s.listen()
    print("Server started successfully...")
except OSError as e:
    print("Port is already in use!")
    print(e)
    exit()
client, address = s.accept()

threading.Thread(
    target=receive,
    args=(listbox,),
    daemon=True
).start()
root.mainloop()
