import tkinter as tk
from tkinter import messagebox

contacts = []


def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    email = email_entry.get()

    if name and number:
        contact = {'name': name, 'number': number, 'email': email}
        contacts.append(contact)
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Number are required fields.")


def search_contact():
    search_name = search_entry.get().lower()
    found_contacts = [contact for contact in contacts if search_name in contact['name'].lower()]

    if found_contacts:
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        for contact in found_contacts:
            result_text.insert(tk.END, f"Name: {contact['name']}\n")
            result_text.insert(tk.END, f"Phone Number: {contact['number']}\n")
            result_text.insert(tk.END, f"Email: {contact['email']}\n")
            result_text.insert(tk.END, "----------------------\n")
        result_text.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("No Contacts", "No contacts found!")


def display_contacts():
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    if contacts:
        for contact in contacts:
            result_text.insert(tk.END, f"Name: {contact['name']}\n")
            result_text.insert(tk.END, f"Phone Number: {contact['number']}\n")
            result_text.insert(tk.END, f"Email: {contact['email']}\n")
            result_text.insert(tk.END, "----------------------\n")
    else:
        result_text.insert(tk.END, "Contact list is empty!\n")
    result_text.config(state=tk.DISABLED)


def remove_contact():
    name_to_remove = remove_entry.get().lower()
    removed = False
    for contact in contacts[:]:
        if name_to_remove == contact['name'].lower():
            contacts.remove(contact)
            removed = True
    if removed:
        messagebox.showinfo("Success", "Contact removed successfully!")
    else:
        messagebox.showinfo("Not Found", "Contact not found!")

    clear_entries()


def clear_entries():
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)
    remove_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Contact List Program")

name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root, width=30)

number_label = tk.Label(root, text="Phone Number:")
number_entry = tk.Entry(root, width=30)

email_label = tk.Label(root, text="Email:")
email_entry = tk.Entry(root, width=30)

add_button = tk.Button(root, text="Add Contact", command=add_contact)

search_label = tk.Label(root, text="Search by Name:")
search_entry = tk.Entry(root, width=30)

search_button = tk.Button(root, text="Search", command=search_contact)

display_button = tk.Button(root, text="Display All Contacts", command=display_contacts)

remove_label = tk.Label(root, text="Remove by Name:")
remove_entry = tk.Entry(root, width=30)

remove_button = tk.Button(root, text="Remove Contact", command=remove_contact)

result_text = tk.Text(root, height=15, width=50, state=tk.DISABLED)

name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
name_entry.grid(row=0, column=1, padx=5, pady=5)

number_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
number_entry.grid(row=1, column=1, padx=5, pady=5)

email_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
email_entry.grid(row=2, column=1, padx=5, pady=5)

add_button.grid(row=3, column=0, columnspan=2, pady=10)

search_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
search_entry.grid(row=4, column=1, padx=5, pady=5)
search_button.grid(row=5, column=0, columnspan=2, pady=10)

display_button.grid(row=6, column=0, columnspan=2, pady=10)

remove_label.grid(row=7, column=0, padx=5, pady=5, sticky=tk.E)
remove_entry.grid(row=7, column=1, padx=5, pady=5)
remove_button.grid(row=8, column=0, columnspan=2, pady=10)

result_text.grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()
