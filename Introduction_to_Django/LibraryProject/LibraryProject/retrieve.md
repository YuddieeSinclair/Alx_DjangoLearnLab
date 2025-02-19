from bookshelf.models import Book

book = Book.objects.all()

for i in book:
    print(i.title, i.author, i.publication_year)


 # 1984 by George Orwell, publication_year: 1949