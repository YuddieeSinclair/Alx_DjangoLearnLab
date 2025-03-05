from relationship_app.models import *

#Query all books by a specific author



#list all books in a library
def my_library(library_name):
    library = Library.objects.get(library_name)
    return my_library.books.all()

for book in book_name:
    print(f"{book.title} by {book.author}")



#retrieve the librarian for a library