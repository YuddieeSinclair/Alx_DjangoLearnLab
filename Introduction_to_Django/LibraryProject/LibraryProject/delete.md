from bookshelf.models import Book

del_book = Book.objects.get(publication_year=1949)
del_book.delete()

book = Book.objects.all()
for i in book:
    print(i.title, i.author, i.publication_year)