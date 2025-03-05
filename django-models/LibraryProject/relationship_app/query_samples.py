from relationship_app.models import *

#Query all books by a specific author



#list all books in a library
def find_library(library_name):
    my_library = Library.objects.get(name=library_name)
    return my_library.books.all()

#retrieve the librarian for a library