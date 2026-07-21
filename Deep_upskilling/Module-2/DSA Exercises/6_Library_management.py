book_collection = [
    "Clean Code",
    "Design Patterns",
    "Refactoring",
    "Domain-Driven Design",
    "Pragmatic Programmer"
]

search_title = "Refactoring"
print(f"Checking availability of: '{search_title}'")

for book in book_collection:
    if book.lower() == search_title.lower():
        print("-> Status: Book is Available in Library")
        break
else:
    print("-> Status: Book Not Found in Collection")