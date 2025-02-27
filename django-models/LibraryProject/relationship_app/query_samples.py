from relationship_app.models import *

#Query all books by a specific author
specific_author = Author.objects.get(author_name="author name")
books_by = specific_author.objects.filter(author=specific_author)
for book in specific_author:
    print(book.title)

#list of all books in a library
all_books = Book.objects.all()
for book in all_books:
    print(book.title)

#Retrieve the librarian for a library.
library = Library.objects.get(Library="library name")
librarian = library.Librarian
print(librarian.name)
