import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4 or length > 64:
            messagebox.showwarning(
                "Warning", "Password length should be between 4 and 64."
            )
            return

        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(length))

        # Ενημέρωση του πεδίου με τον νέο κωδικό
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")


def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:

        messagebox.showwarning("Warning", "No password to copy!")


# 1. Δημιουργία Κύριου Παραθύρου
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)

# 2. Widgets (Ετικέτες, Πεδία, Κουμπιά)
title_label = tk.Label(
    root, text="Password Generator", font=("Helvetica", 16, "bold")
)
title_label.pack(pady=10)

# Πεδίο για το Μήκος Κωδικού
frame_length = tk.Frame(root)
frame_length.pack(pady=5)

length_label = tk.Label(frame_length, text="Password Length:")
length_label.pack(side=tk.LEFT, padx=5)

length_entry = tk.Entry(frame_length, width=5)
length_entry.insert(0, "12")  # Προεπιλεγμένη τιμή
length_entry.pack(side=tk.LEFT)

# Κουμπί Δημιουργίας
generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="#4CAF50",
    fg="white",
)
generate_btn.pack(pady=10)

# Πεδίο Εμφάνισης Κωδικού
password_entry = tk.Entry(
    root, font=("Courier", 12), width=30, justify="center"
)
password_entry.pack(pady=5)

# Κουμπί Αντιγραφής
copy_btn = tk.Button(
    root, text="Copy to Clipboard", command=copy_to_clipboard
)
copy_btn.pack(pady=5)

# 3. Εκκίνηση του Event Loop
root.mainloop()
