from relationship_app.models import *

#Query all books by a specific author
def query_all_books(author_name):
    my_author = Author.objects.get(author=author_name)
    return my_author.objects.filter(author_name)



#list all books in a library
def find_library(library_name):
    my_library = Library.objects.get(name=library_name)
    return my_library.books.all()

#retrieve the librarian for a library