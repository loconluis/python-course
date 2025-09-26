class Book:
    def __init__(self, title: str):
        self.title: str = title
        self.available: bool = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"Book with title: {self.title} borrowed successfully.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"Book with title: {self.title} returned successfully.")


class User:
    def __init__(self, name: str, userid: int):
        self.name: str = name
        self.userid: int = userid
        self.books: list[Book] = []

    def borrow_book(self, book: Book):
        if book.available:
            book.borrow()
            self.books.append(book)
        else:
            print(f"Book with title: {book.title} is not available.")

    def return_book(self, book: Book):
        if book in self.books:
            book.return_book()
            self.books.remove(book)
        else:
            print(f"Book with title: {book.title} is not borrowed by you.")


class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.users: list[User] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"Book with title: {book.title} is not available in the library.")

    def register_user(self, user: User):
        self.users.append(user)

    def unregister_user(self, user: User):
        if user in self.users:
            self.users.remove(user)
        else:
            print(f"User with id: {user.userid} is not registered in the library.")

    def show_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Available: {book.available}")

    def show_users(self):
        for user in self.users:
            print(f"Name: {user.name}, ID: {user.userid}")


book1 = Book("Python Programming")
book2 = Book("Java Programming")
library = Library()
library.add_book(book1)
library.add_book(book2)
u1 = User("John Doe", 1)
u2 = User("Jane Doe", 2)
library.register_user(u1)
library.register_user(u2)
u1.borrow_book(book1)

library.show_books()
library.show_users()
