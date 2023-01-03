from tkinter import *
from tkinter import messagebox
from sms import send_sms
from gen import generate_nicety


class Interface:

    def __init__(self):
        """Initialize the interface."""
        self.root = Tk()
        self.root.title("Interface")
        self.root.config(pady=50, padx=50)

        # img
        self.img = PhotoImage(file="Someone Special.png")
        self.label = Label(image=self.img)
        self.label.grid(row=0, column=0, columnspan=2)

        # canvas

        self.phone_label = Label(text="Phone: ")
        self.phone_label.grid(row=1, column=0)
        self.user_message_label = Label(text="User Message:")
        self.user_message_label.grid(row=2, column=0)

        # entrys
        self.phone_entry = Entry(width=35)
        self.phone_entry.insert(END, "+1")
        self.phone_entry.grid(row=1, column=1, pady=10)
        self.user_message_entry = Text(height=15, width=40, wrap=WORD)
        self.user_message_entry.insert(END,
                                       "Write your message here, or click 'Generate Message' to generate a message.")
        self.user_message_entry.grid(row=2, column=1)
        # make user message entry larger text
        self.user_message_entry.config(font=("Arial", 16))

        # buttons
        self.generate_message_button = Button(text="Generate Message", command=self.generate)
        self.generate_message_button.grid(row=3, column=1)
        self.send_button = Button(text="Send", command=self.send)
        self.send_button.grid(row=3, column=2)

        self.root.mainloop()

    def send(self):
        """Send SMS message to user."""
        message = self.user_message_entry.get(1.0, END)
        phone = self.phone_entry.get()
        send_sms(message, phone)
        # confirmation box:
        messagebox.showinfo(title="Message Sent", message="Message Sent", parent=self.root)

        # clear entry boxes
        self.user_message_entry.delete(1.0, END)
        self.phone_entry.delete(0, END)

    def generate(self):
        """Generate a message."""
        message = generate_nicety()
        self.user_message_entry.delete(1.0, END)
        self.user_message_entry.insert(END, message)


