import threading
import socket
import tkinter as tk
import threading
import socket
alias = input('Choose an alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
# Create the main window
window = tk.Tk()
window.title("Chat Application  Hi," + alias)

# Configure the window size and background color
window.geometry("500x500")
window.configure(bg="#f2f2f2")

# Create a frame for the messages
messages_frame = tk.Frame(window, bg="#f2f2f2")
messages_frame.pack(pady=10)

# Create a text box to display messages
messages_textbox = tk.Text(messages_frame, width=50, height=20, bg="white", fg="black", font=("Helvetica", 12))
messages_textbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

# Create a scrollbar for the messages
scrollbar = tk.Scrollbar(messages_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the scrollbar to work with the messages_textbox
messages_textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=messages_textbox.yview)

# Create a frame for the input box and send button
input_frame = tk.Frame(window, bg="#f2f2f2")
input_frame.pack(pady=10)

# Create an input box for sending messages
input_box = tk.Entry(input_frame, width=40, font=("Helvetica", 12))
input_box.pack(side=tk.LEFT, padx=10)

# Create a send button
send_button = tk.Button(input_frame, text="Send", font=("Helvetica", 12), bg="#4caf50", fg="white", padx=10)
send_button.pack(side=tk.LEFT)

# Create a function to handle sending messages
def send_message(event=None):
    message = input_box.get()
    client.send(f'{alias}: {message}'.encode('utf-8'))
    input_box.delete(0, tk.END)

# Bind the Enter key and send button to the send_message function
window.bind('<Return>', send_message)
send_button.configure(command=send_message)

# Create a function to update the messages_textbox
def update_messages(message):
    messages_textbox.insert(tk.END, message + '\n')
    messages_textbox.see(tk.END)

# Function to handle receiving messages
def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                update_messages(message)
        except:
            update_messages('Error!')
            client.close()
            break

# Create a thread to handle receiving messages
receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

# Create a function to handle closing the window
def close_window():
    client.close()
    window.destroy()

# Set the close_window function as the handler for the window close event
window.protocol("WM_DELETE_WINDOW", close_window)

# Start the GUI main loop
window.mainloop()
