import tkinter as tk
from tkinter import ttk
import psycopg2


class AddressBook(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Address Book")
        self.geometry("800x300")

        # Create notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, padx=10)

        # Create tabs
        self.create_tab = ttk.Frame(self.notebook)
        self.update_tab = ttk.Frame(self.notebook)
        self.delete_tab = ttk.Frame(self.notebook)
        self.view_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.create_tab, text="Create Contact")
        self.notebook.add(self.update_tab, text="Update Contact")
        self.notebook.add(self.delete_tab, text="Delete Contact")
        self.notebook.add(self.view_tab, text="View Contacts")

        # Create widgets for create tab
        self.first_name_label = ttk.Label(self.create_tab, text="First Name")
        self.first_name_label.grid(row=0, column=0, padx=5, pady=5)

        self.first_name_entry = ttk.Entry(self.create_tab)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.last_name_label = ttk.Label(self.create_tab, text="Last Name")
        self.last_name_label.grid(row=1, column=0, padx=5, pady=5)

        self.last_name_entry = ttk.Entry(self.create_tab)
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = ttk.Label(self.create_tab, text="Email")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)

        self.email_entry = ttk.Entry(self.create_tab)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.phone_label = ttk.Label(self.create_tab, text="Phone")
        self.phone_label.grid(row=3, column=0, padx=5, pady=5)

        self.phone_entry = ttk.Entry(self.create_tab)
        self.phone_entry.grid(row=3, column=1, padx=5, pady=5)

        self.create_button = ttk.Button(self.create_tab, text="Create Contact", command=self.create_contact)
        self.create_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Create widgets for update tab
        self.id_label = ttk.Label(self.update_tab, text="ID")
        self.id_label.grid(row=0, column=0, padx=5, pady=5)

        self.id_entry = ttk.Entry(self.update_tab)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.update_first_name_label = ttk.Label(self.update_tab, text="First Name")
        self.update_first_name_label.grid(row=1, column=0, padx=5, pady=5)

        self.update_first_name_entry = ttk.Entry(self.update_tab)
        self.update_first_name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.update_last_name_label = ttk.Label(self.update_tab, text="Last Name")
        self.update_last_name_label.grid(row=2, column=0, padx=5, pady=5)

        self.update_last_name_entry = ttk.Entry(self.update_tab)
        self.update_last_name_entry.grid(row=2, column=1, padx=5, pady=5)

        self.update_email_label = ttk.Label(self.update_tab, text="Email")
        self.update_email_label.grid(row=3, column=0, padx=5, pady=5)

        self.update_email_entry = ttk.Entry(self.update_tab)
        self.update_email_entry.grid(row=3, column=1, padx=5, pady=5)

        self.update_phone_label = ttk.Label(self.update_tab, text="Phone")
        self.update_phone_label.grid(row=4, column=0, padx=5, pady=5)

        self.update_phone_entry = ttk.Entry(self.update_tab)
        self.update_phone_entry.grid(row=4, column=1, padx=5, pady=5)

        self.update_button = ttk.Button(self.update_tab, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Widget to delete a contact
        # Create input field for first name
        self.delete_first_name_label = tk.Label(self.delete_tab, text="First Name:")
        self.delete_first_name_label.grid(row=0, column=0, padx=5, pady=5)
        self.delete_first_name_entry = tk.Entry(self.delete_tab)
        self.delete_first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create delete button
        self.delete_button = tk.Button(self.delete_tab, text="Delete", command=self.delete_contact_by_name)
        self.delete_button.grid(row=1, column=1, padx=5, pady=5)

        # Widget to Display all Contacts
        self.view_tab_button = tk.Button(self.view_tab, text="Display All Contacts", command=self.fetch_all_contacts)
        self.view_tab_button.grid(row=1, column=1, padx=5, pady=5)

    def create_contact(self):
        # Connect to database
        conn = psycopg2.connect(database="address_book", user="postgres", password="1122", host="localhost",
                                port="8899")
        cur = conn.cursor()

        # Get values from entries
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        # Insert values into database
        cur.execute("INSERT INTO contacts (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)",
                    (first_name, last_name, email, phone))

        # Commit changes and close connection
        conn.commit()
        conn.close()

        # Clear entries
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

        # Display success message
        success_message = "Contact Added Successfully"
        success_label = tk.Label(self.create_tab, text=success_message)
        success_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def update_contact(self):
        # Connect to database
        conn = psycopg2.connect(database="address_book", user="postgres", password="1122", host="localhost",
                                port="8899")
        cur = conn.cursor()

        # Get values from entries
        id = self.id_entry.get()
        first_name = self.update_first_name_entry.get()
        last_name = self.update_last_name_entry.get()
        email = self.update_email_entry.get()
        phone = self.update_phone_entry.get()

        # Update values in database
        cur.execute("UPDATE contacts SET first_name=%s, last_name=%s, email=%s, phone=%s WHERE id=%s",
                    (first_name, last_name, email, phone, id))

        # Commit changes and close connection
        conn.commit()
        conn.close()

        # Clear entries
        self.id_entry.delete(0, tk.END)
        self.update_first_name_entry.delete(0, tk.END)
        self.update_last_name_entry.delete(0, tk.END)
        self.update_email_entry.delete(0, tk.END)
        self.update_phone_entry.delete(0, tk.END)

        update_message = "Contact Updated Successfully!!!"
        update_label = tk.Label(self.update_tab, text=update_message)
        update_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def delete_contact_by_name(self):
        # Connect to database
        conn = psycopg2.connect(database="address_book", user="postgres", password="1122", host="localhost",
                                port="8899")
        cur = conn.cursor()

        # Get value from entry
        first_name = self.delete_first_name_entry.get()

        # Delete contact from database
        cur.execute("DELETE FROM contacts WHERE first_name=%s", (first_name,))

        # Commit changes and close connection
        conn.commit()
        conn.close()

        # Clear entry
        self.delete_first_name_entry.delete(0, tk.END)

        # Showing Delete Message
        delete_message = "Contact Deleted Successfully!!!"
        delete_label = tk.Label(self.delete_tab, text=delete_message)
        delete_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def fetch_all_contacts(self):
        # Connect to database
        conn = psycopg2.connect(database="address_book", user="postgres", password="1122", host="localhost",
                                port="8899")
        cur = conn.cursor()

        # Fetch all contacts from database
        cur.execute("SELECT * FROM contacts")
        rows = cur.fetchall()

        # Create a new window to display contacts
        top = tk.Toplevel()
        top.title("All Contacts")
        top.geometry("800x300")

        # Create treeview widget
        tree = ttk.Treeview(top)
        tree["columns"] = ("ID", "First Name", "Last Name", "Email", "Phone")

        # Define columns
        tree.column("#0", width=0, stretch=False)
        tree.column("ID", anchor="center", width=80)
        tree.column("First Name", anchor="center", width=100)
        tree.column("Last Name", anchor="center", width=100)
        tree.column("Email", anchor="center", width=150)
        tree.column("Phone", anchor="center", width=120)

        # Define column headings
        tree.heading("#0", text="")
        tree.heading("ID", text="ID")
        tree.heading("First Name", text="First Name")
        tree.heading("Last Name", text="Last Name")
        tree.heading("Email", text="Email")
        tree.heading("Phone", text="Phone")

        # Add contacts to treeview
        for row in rows:
            tree.insert("", tk.END, values=row)

        tree.pack(expand=True, fill="both")

        # Close connection
        conn.close()


if __name__ == "__main__":
    address_book = AddressBook()
    address_book.mainloop()
