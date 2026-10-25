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
             self.availability_status = False
             print(f'You can borrow {self.title} book.')
        else:
            print('This book is not available.')
        
    def return_book(self):
         if self.availability_status == False:
            self.availability_status = True
            print(f'{self.title} has been returned to the library. ')
         else:
             print(f'{self.title} book was already in the shelf.')




class Library:
    def __init__(self):
        self.books =[] 

    def add_books(self,book):
      self.books.append(book) 

    
    def display_all(self):
        print('--- Library Books ---')
        for book in self.books:
            book.book_details()

    def find_book(self, search):
        search = str(search).lower() 
        for book in self.books:
            if search == str(book.book_id).lower() or search in book.title.lower():
                return book  
        print('Book cannot be found.')
        
my_library=Library() 
        
my_library.add_books(Book('104', 'Muna Madan', 'Laxmi Prasad Devkota', True))
my_library.add_books(Book('105', 'Palpasa Cafe', 'Narayan Wagle', True))
my_library.add_books(Book('106', 'Seto Bagh', 'Diamond Shumsher Rana', True))
my_library.add_books(Book('107', 'Karnali Blues', 'Buddhisagar', True))


while True:
    print('\n--Library Menu -- ')
    print('1.  Display All')
    print('2. Search')
    print('3. Borrow')
    print('4. Return')
    print('5. Exit')

    choice = input(' Enter choice (1-5): ')

    if choice == '1':
        my_library.display_all()

    elif choice == '2':
        search = my_library.find_book(input('Search Id of the book  or The Title: '))
        if search: 
            search.book_details()

    elif choice == '3':
        borrow = my_library.find_book(input('Borrow ID or Title: ')) 
        if borrow: 
            borrow.borrow_books()

    elif choice == '4':
        return_result = my_library.find_book(input('Return ID or Title: '))
        if return_result: 
            return_result.return_book()

    elif choice == '5':
        print('Goodbye!')
        break

