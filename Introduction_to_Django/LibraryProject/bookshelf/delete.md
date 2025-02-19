from bookshelf.models import Book

del_book = Book.objects.filter(publication_year=1949).delete()

book = Book.objects.all()
for i in book:
    print(i.title, i.author, i.publication_year)