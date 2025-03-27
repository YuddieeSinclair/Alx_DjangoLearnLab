from bookshel.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# 1984 by George Orwell, publication_year: 1949
