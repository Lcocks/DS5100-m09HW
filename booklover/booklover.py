#booklover.py
import pandas as pd

class BookLover():
    """
    A set of methods to record and displays your favorite books.
    """

    num_books = 0
    book_list = pd.DataFrame({'book_name': [], 'book_rating': []})

    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name': [], 'book_rating': []})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self, book_name, rating):
        new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [int(rating)]
        })
        if not(new_book.book_name.values in self.book_list.book_name.values):
            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
        else:
            print('Book already added.')
        #self.book_list = pd.concat([self.book_list, new_book], ignore_index = True) if not(new_book.book_name.values in self.book_list.book_name.values) else print('Book already added.')
        
    def has_read(self, book_name):
        return True if book_name in self.book_list.book_name.values else False
    
    def num_books_read(self):
        self.num_books = len(self.book_list.index)
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list.book_rating >= 3]
        
        
