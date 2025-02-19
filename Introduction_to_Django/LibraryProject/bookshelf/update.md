from bookshelf.models import Book

update_book = Book.objects.filter(title="1984").update(title= 'Nineteen Eighty-Four')
print(update_book)

# Nineteen Eighty-Four by George Orwell, publication_year: 1949