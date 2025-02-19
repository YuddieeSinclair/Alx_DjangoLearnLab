from bookshelf.models import Book

book = Book.objects.get(publication_year=1949)
book.delete()

# del_book = Book.delete() 

book = Book.objects.all()
for i in book:
    print(i.title, i.author, i.publication_year)

