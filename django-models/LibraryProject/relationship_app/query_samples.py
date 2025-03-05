from relationship_app.models import *

#Query all books by a specific author



#list all books in a library
library_name = ""
my_library = Library.objects.get(library_name)
book_name = my_library.books.all()

for book in book_name:
    print(f"{book.title} by {book.author}")



#retrieve the librarian for a library