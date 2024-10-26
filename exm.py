# A
# B A
# C B A


a=65
for i in range(3):
    for j in range(i+1):
        print(chr(a-j),end='\t')
    print()
    a+=1







    # Initialize the library as a list of dictionaries
library = []

# Start the library management system
while True:
    print("\nLibrary Management Options:")
    print("1. Add Book\n2. Update Book\n3. Remove Book\n4. View All Books\n5. Search Book\n6. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        # Add a new book
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        genre = input("Enter Genre: ")

        # Check if the book ID already exists
        if any(book['Book ID'] == book_id for book in library):
            print("Book ID already exists. Try another ID.")
        else:
            book = {
                'Book ID': book_id,
                'Title': title,
                'Author': author,
                'Genre': genre
            }
            library.append(book)
            print(f"Book '{title}' added successfully.")

    elif choice == '2':
        # Update an existing book
        book_id = input("Enter Book ID to update: ")
        found = False

        for book in library:
            if book['Book ID'] == book_id:
                title = input("Enter new Book Title: ")
                author = input("Enter new Author: ")
                genre = input("Enter new Genre: ")
                book['Title'] = title
                book['Author'] = author
                book['Genre'] = genre
                print(f"Book ID '{book_id}' updated successfully.")
                found = True
                break
        
        if not found:
            print("Book not found.")

    elif choice == '3':
        # Remove a book
        book_id = input("Enter Book ID to remove: ")
        found = False

        for book in library:
            if book['Book ID'] == book_id:
                library.remove(book)
                print(f"Book ID '{book_id}' removed successfully.")
                found = True
                break
        
        if not found:
            print("Book not found.")

    elif choice == '4':
        # View all books
        if library:
            for book in library:
                print(f"\nBook ID: {book['Book ID']}")
                print(f"Title: {book['Title']}")
                print(f"Author: {book['Author']}")
                print(f"Genre: {book['Genre']}")
        else:
            print("No books in the library.")

    elif choice == '5':
        # Search for a book
        book_id = input("Enter Book ID to search: ")
        found = False

        for book in library:
            if book['Book ID'] == book_id:
                print(f"\nBook ID: {book['Book ID']}")
                print(f"Title: {book['Title']}")
                print(f"Author: {book['Author']}")
                print(f"Genre: {book['Genre']}")
                found = True
                break
        
        if not found:
            print("Book not found.")

    elif choice == '6':
        # Exit the program
        print("Exiting Library Management.")
        break

    else:
        print("Invalid choice. Try again.")
