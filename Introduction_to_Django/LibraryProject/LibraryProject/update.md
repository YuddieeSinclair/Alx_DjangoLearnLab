from bookshelf.models import Book

update_book = Book.objects.get(author="George Orwell")
update_book.title = 'Nineteen Eighty-Four'
update_book.save()

# print(update_book)
# Nineteen Eighty-Four by George Orwell, publication_year: 1949