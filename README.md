# Python Socket Chat Application (Tkinter GUI)

## Overview

This project is a simple **real-time chat application** built using Python.
It uses:

* **Socket Programming** for communication
* **Tkinter** for graphical user interface (GUI)

The application allows a **client and server** to exchange messages in real-time.


## Features

* Real-time communication using sockets
* GUI-based chat interface using Tkinter
* Continuous messaging using loops
* Separate send and receive functions


## Technologies Used

* Python 3
* Socket Module
* Tkinter Library


## Project Structure

```
ChatApp/
│── server.py
│── client.py
│── layout.py
│── README.md
```


## How It Works

1. The **server** starts and waits for a connection.
2. The **client** connects to the server using IP address and port.
3. Once connected, both can:

   * Send messages
   * Receive messages
4. Messages are displayed in the GUI chat window.


## How to Run

### Step 1: Run Server

```bash
python server_gui.py
```

### Step 2: Run Client (in another terminal)

```bash
python client_gui.py
```


### Socket Programming

Used to establish communication between client and server.

### Tkinter GUI

Provides a user-friendly chat interface.


## Future Enhancements

* Multi-user group chat
* Improved UI design
* Emoji support
* User authentication system
* Internet-based communication


## Author

**Mayuri Bhavsar**
