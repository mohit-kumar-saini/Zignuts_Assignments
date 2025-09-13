class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, title):
        self.books.append(title)
        print("Added book:", title)

    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
            print("Removed book:", title)
        else:
            print("Book not found:", title)

    def search_book(self, title):
        if title in self.books:
            print("Book found:", title)
        else:
            print("Book not found:", title)

library = Library()
library.add_book("Python Basics")
library.add_book("Data Structures")
library.add_book("Artificial Intelligence")
library.add_book("Machine Learning")
library.search_book("Python Basics")
library.remove_book("Data Structures")
library.search_book("Data Structures")
