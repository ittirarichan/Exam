# ----------------library Management----------------

l=[]

# ----------------Adding Book----------------

def add_book():
    book ={}
    book["title"] = input("Enter the Book Title :")
    book["author"] = input("Enter the auther Name :")
    book["year"] = input("Enter the publication year: ")
    book["sn"] = input("Enter the Serial number: ")
    l.append(book)
    print(f"Book '"+ book['title']+"' Added")

# ----------------Update Book----------------:)
def update_book():
    search_title = input("Enter the title of the book to update: ")
    for book in l:
        if book["title"].lower() == search_title.lower():
            print("Book found. Enter new details.")
            book["title"] = input("Enter new book title: ")
            book["author"] = input("Enter new author name: ")
            book["year"] = input("Enter new publication year: ")
            book["sn"] = input("Enter new serial number: ")
            print(f"Book '{book['title']}' updated successfully!\n")
            return
    print("Book not found")



# ----------------Remove Book----------------

def remove_book():
    search_title = input("Enter the title of the book to remove: ")
    for book in l:
        if book['title'].lower() == search_title.lower():
            l.remove(book)
            print(f"Book '{search_title}' removed successfully!\n")
            return
    print("Book not found")

# ----------------View Book----------------
def view_book():
    if not l:
        print("No Books Available in this library")
    else:
        print("Available Books in this library")
        for idx, book in enumerate(l, 1):
            print(f"{idx}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, SN: {book['sn']}")
        print() 

# ----------------Search Book----------------
def search_book():
    search_title = input("Enter the title of the book to search: ")
    for book in l:
        if book['title'].lower() == search_title.lower():
            print(f"Book found: Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, SN: {book['sn']}")
            return
    print("Book not found")
3

# ----------------Main----------------
def main():
    while True:
        print("Welcome to the Library Management System!")
        print("1. Add book")
        print("2. Update book")
        print("3. Remove book")
        print("4. View all books")
        print("5. Search book")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            remove_book()
        elif choice == '4':
            view_book()
        elif choice == '5':
            search_book()
        elif choice == '6':
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()