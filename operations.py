# library/operations.py
# Mini Library Management System

genres = ("Fiction", "Non-Fiction", "Sci-Fi")

books = {}
members = []

def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        print("Book with this ISBN already exists.")
        return
    if genre not in genres:
        print("Invalid genre. Please choose from:", genres)
        return
    books[isbn] = {"title": title, "author": author, "genre": genre, "total_copies": total_copies}
    print(f"Book '{title}' added successfully.")

def add_member(member_id, name, email):
    for member in members:
        if member["member_id"] == member_id:
            print("Member ID already exists.")
            return
    members.append({"member_id": member_id, "name": name, "email": email, "borrowed_books": []})
    print(f"Member '{name}' added successfully.")

def search_books(keyword):
    results = []
    for isbn, details in books.items():
        if keyword.lower() in details["title"].lower() or keyword.lower() in details["author"].lower():
            results.append((isbn, details))
    if results:
        print("Search Results:")
        for isbn, details in results:
            print(f"ISBN: {isbn}, Title: {details['title']}, Author: {details['author']}")
    else:
        print("No matching books found.")

def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        print("Book not found.")
        return
    if genre and genre not in genres:
        print("Invalid genre.")
        return
    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if genre:
        books[isbn]["genre"] = genre
    if total_copies is not None:
        books[isbn]["total_copies"] = total_copies
    print(f"Book '{isbn}' updated successfully.")

def update_member(member_id, name=None, email=None):
    for member in members:
        if member["member_id"] == member_id:
            if name:
                member["name"] = name
            if email:
                member["email"] = email
            print(f"Member '{member_id}' updated successfully.")
            return
    print("Member not found.")

def delete_book(isbn):
    if isbn not in books:
        print("Book not found.")
        return
    for member in members:
        if isbn in member["borrowed_books"]:
            print("Cannot delete book. It is currently borrowed.")
            return
    del books[isbn]
    print("Book deleted successfully.")

def delete_member(member_id):
    for member in members:
        if member["member_id"] == member_id:
            if member["borrowed_books"]:
                print("Cannot delete member. They have borrowed books.")
                return
            members.remove(member)
            print("Member deleted successfully.")
            return
    print("Member not found.")

def borrow_book(member_id, isbn):
    for member in members:
        if member["member_id"] == member_id:
            if len(member["borrowed_books"]) >= 3:
                print("Member already borrowed maximum of 3 books.")
                return
            if isbn not in books:
                print("Book not found.")
                return
            if books[isbn]["total_copies"] <= 0:
                print("No copies available.")
                return
            member["borrowed_books"].append(isbn)
            books[isbn]["total_copies"] -= 1
            print(f"Book '{books[isbn]['title']}' borrowed successfully by {member['name']}.")
            return
    print("Member not found.")

def return_book(member_id, isbn):
    for member in members:
        if member["member_id"] == member_id:
            if isbn not in member["borrowed_books"]:
                print("This member did not borrow that book.")
                return
            member["borrowed_books"].remove(isbn)
            books[isbn]["total_copies"] += 1
            print(f"Book '{books[isbn]['title']}' returned successfully by {member['name']}.")
            return
    print("Member not found.")