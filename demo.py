# library/demo.py
from operations import *

print("=== DEMO: MINI LIBRARY MANAGEMENT SYSTEM ===\n")

# Add books
add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 4)
add_book("B002", "A Brief History of Time", "Stephen Hawking", "Non-Fiction", 2)
add_book("B003", "Dune", "Frank Herbert", "Sci-Fi", 3)

# Add members
add_member(1, "John Doe", "john@example.com")
add_member(2, "Jane Smith", "jane@example.com")

# Borrow and return books
borrow_book(1, "B001")
borrow_book(1, "B002")
return_book(1, "B001")

# Search
search_books("Dune")

# Update and delete
update_book("B003", total_copies=5)
update_member(2, name="Jane Johnson")
delete_book("B001")
delete_member(2)

print("\n=== DEMO COMPLETE ===")