from bookshelf.models import Book

book = Book.objects.get(title="1984")

print(book)
 # 1984 by George Orwell, publication_year: 1949