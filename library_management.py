lib = []

while True:
    print("Choice: ")
    print("\n1.Add Book 2.Update Book 3.Remove Book 4.View All Books 5.Search Books 6.Exit")
    choice = int(input("Enter Choice :"))


    if choice == 1 :
        book_id = int(input("Enter Book ID: "))
        title = input("Enter the Title: ")
        author = input("Enter Author: ")
        type = input("Enter Type: ")


        if any(book['Book_ID'] == book_id for book in lib):
            print("Book ID Exists,Try another ID ")
        else:
            book = {
                'Book ID' : book_id,
                'Title' : title,
                'Author' : author,
                'Type' : type
            }

            lib.append(book)
            print("Book '{title}' added successfully")

    elif choice == 2 :
        book_id = int(input("Enter Book ID: "))
        found = False 

        for book in lib:
            if book['Book ID'] == book_id:
                 title = input("Enter the Title: ")
                 author = input("Enter Author: ")
                 type = input("Enter Type: ")
                 book['Title'] = title
                 book['Author'] = author
                 book['Type'] = type
                 print("Book ID '{book_id}' added successfully")
                 found = True
                 break
        if not found:
            print("Book Not found ")
    
    elif choice == 3 :
        book_id = input("Enter Book ID to remove: ")
        found = False
        
        for book in lib:
            if book['Book ID'] == book_id:
                lib.remove(book)
                print("Book ID '{book_id}' removed successfully")
                found = True
                break
        
        if not found:
            print("Book not found")
    
    elif choice == 4:
        if lib:
            for book in lib:
                print(f"\nBook ID: {book['Book ID']}")
                print(f"Title: {book['Title']}")
                print(f"Author: {book['Author']}")
                print(f"Type: {book['Type']}")
        else:
            print("No Book in the Library ")
    elif choice == 5:
        book_id = int(input("Enter ID to search: "))
        found = False

        for book in lib:
            if book ['Book ID'] == book_id:
                print(f"\nBook ID: {book['Book ID']}")
                print(f"Title: {book['Title']}")
                print(f"Author: {book['Author']}")
                print(f"Type: {book['Type']}")
                found = True
                break

        if not found:
            print("Book not Found")

    elif choice == 6:
        print("Exiting....")
        break
    else:
        print("Enterd an invalid choice, Try agin")


