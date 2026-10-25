# Develop a simple library management program using Python functions and OOP.

# Requirements:

# - Create a "Book" class with attributes such as book ID, title, author, and availability status.
# - Create methods to display book details, borrow a book, and return a book.
# - Allow users to display all books and search for a book by ID or title.
# - Display appropriate messages when a book is unavailable or cannot be found


class Book:
    def __init__(self , book_id , title , author , availability_status):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability_status = availability_status


    def book_details(self):
        print(f'Book Id: {self.book_id}')
        print(f'Titile: {self.title}')
        print(f'Author: {self.author}')
        print(f'Avalailability Status: {self.availability_status}')


    def borrow_books(self):
        if self.availability_status == True:
             self.availability_status == False
             print(f'You can borrow {self.title} book.')
        else:
            print('This book is not available.')
        
    def return_book(self):
         if self.availability_status == False:
            self.availability_status = True
            print(f'{self.title} has been returned to the library. ')
         else:
             print(f'{self.title} book was already in the shelf.')




