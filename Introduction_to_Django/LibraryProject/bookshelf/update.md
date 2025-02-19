from bookshelf.models import Book

update_book = Book.objects.filter(author="George Orwell").update(title= 'Nineteen Eighty-Four')
print(update_book)

# Nineteen Eighty-Four by George Orwell, publication_year: 1949