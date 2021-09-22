import pdb

from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Rick", "Riordan")
author_repository.save(author_1)
author_2 = Author("Jesus", "Christ")
author_repository.save(author_2)
author_3 = Author("JRR", "Tolkien")
author_repository.save(author_3)

all_authors = author_repository.select_all()

book_1 = Book("Percy Jackson", author_1)
book_repository.save(book_1)
book_2 = Book("Bible", author_2)
book_repository.save(book_2)
book_3 = Book("LOTR", author_3)
book_repository.save(book_3)


single_author = author_repository.select(author_1.id)
single_book = book_repository.select(book_1.id)
all_books = book_repository.select_all()

# book_repository.delete(book_1.id)
# author_repository.delete(author_1.id)

pdb.set_trace()
