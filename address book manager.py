import csv

class Entry:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class AddressBook:
    def __init__(self):
        self.entries = []
    
    def read_entries_from_file(self, filename):
      with open(filename, 'r', encoding='latin-1') as file:
        reader = csv.reader(file)
        for row in reader:
            name, email, phone, address = row
            entry = Entry(name, email, phone, address)
            self.entries.append(entry)
    print("Entries loaded from file.")

    
    def save_entries_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for entry in self.entries:
                writer.writerow([entry.name, entry.email, entry.phone, entry.address])
        print("Entries saved to file.")
    
    def add_entry(self, name, email, phone, address):
        for entry in self.entries:
            if entry.email.lower() == email.lower():
                print("Email already exists. Entry not added.")
                return
        new_entry = Entry(name, email, phone, address)
        self.entries.append(new_entry)
        self.sort_entries()
        print("Entry added.")
    
    def remove_entry(self, email):
        for entry in self.entries:
            if entry.email.lower() == email.lower():
                self.entries.remove(entry)
                print("Entry removed.")
                return
        print("Entry not found.")
    
    def update_entry(self, name, email, phone, address):
        for entry in self.entries:
            if entry.email.lower() == email.lower():
                entry.name = name
                entry.phone = phone
                entry.address = address
                self.sort_entries()
                print("Entry updated.")
                return
        print("Entry not found.")
    
    def search_entries(self, keyword):
        results = []
        for entry in self.entries:
            if keyword.lower() in entry.name.lower() or keyword.lower() in entry.email.lower() or \
               keyword.lower() in entry.phone.lower() or keyword.lower() in entry.address.lower():
                results.append(entry)
        if results:
            print("Search results:")
            for entry in results:
                print(f"Name: {entry.name}\nEmail: {entry.email}\nPhone: {entry.phone}\nAddress: {entry.address}\n")
        else:
            print("No matching entries found.")
    
    def print_all_entries(self):
        if self.entries:
            print("All entries:")
            for entry in self.entries:
                print(f"Name: {entry.name}\nEmail: {entry.email}\nPhone: {entry.phone}\nAddress: {entry.address}\n")
        else:
            print("No entries found.")
    
    def validate_email(self, email):
        for entry in self.entries:
            if entry.email.lower() == email.lower():
                return False
        return True
    
    def sort_entries(self):
        self.entries = sorted(self.entries, key=lambda entry: entry.name.lower())

def main():
    address_book = AddressBook()

    while True:
        action = input("Enter an action keyword (Read, Add, Remove, Update, Search, Print, Save): ").lower()

        if action == "read":
            filename = input("Enter the file name: ")
            address_book.read_entries_from_file(filename)

        elif action == "add":
            entry_data = input("Enter the entry details (name, email, phone, address): ")
            name, email, phone, address = entry_data.split(",")
            if address_book.validate_email(email.strip()):
                address_book.add_entry(name.strip(), email.strip(), phone.strip(), address.strip())
            else:
                print("Email already exists. Entry not added.")

        elif action == "remove":
            email = input("Enter the email of the entry to remove: ")
            address_book.remove_entry(email.strip())

        elif action == "update":
            entry_data = input("Enter the entry details (name, email, phone, address): ")
            name, email, phone, address = entry_data.split(",")
            address_book.update_entry(name.strip(), email.strip(), phone.strip(), address.strip())

        elif action == "search":
            keyword = input("Enter a keyword to search: ")
            address_book.search_entries(keyword.strip())

        elif action == "print":
            address_book.print_all_entries()

        elif action == "save":
            filename = input("Enter the file name to save: ")
            address_book.save_entries_to_file(filename)

        else:
            print("Invalid action keyword. Please try again.")

if __name__ == "__main__":
    main()