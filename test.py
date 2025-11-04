# library/test.py
from operations import *

print("=== TESTING MINI LIBRARY SYSTEM ===\n")

# Add Books
add_book("B101", "1984", "George Orwell", "Fiction", 5)
add_book("B102", "Sapiens", "Yuval Noah Harari", "Non-Fiction", 3)

# Add Members
add_member(1, "Alice", "alice@example.com")
add_member(2, "Bob", "bob@example.com")

# Borrow Books
borrow_book(1, "B101")
borrow_book(1, "B102")

# Return Book
return_book(1, "B101")

# Update Data
update_book("B102", total_copies=10)
update_member(2, email="bob.new@example.com")

# Delete Records
delete_book("B102")
delete_member(2)

# Search
search_books("1984")

print("\n=== TESTS COMPLETE ===")