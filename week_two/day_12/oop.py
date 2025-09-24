"""Library Management System (OOP-heavy)"""
"""Description"""
"""Build a mini-library management system that handles books, members,"""
"""and transactions. This system should allow members to borrow, return,"""
"""and search books. Librarians manage the inventory and enforce borrowing"""
"""limits."""


class Library:

    __books = dict()
    __records = dict()

    # def __init__(self, books=None, records=None):
    #     self.__books = books or {}
    #     self.__records = records or {}

    @staticmethod
    def check_valid_bookname(book_name):
        if len(book_name) < 3:
            raise ValueError(
                "Invalid Book name , name should be at least of 3 character."
            )
        return book_name

    def get_books(self):
        available_books = []

        for book, count in self.__books.items():
            if count > 0:
                available_books.append(book)
        if len(available_books):
            return print(", ".join(available_books))
        else:
            return print("No Books to Borrow and Read")

    # @staticmethod
    def add_book(self, book_name):

        bookname = Library.check_valid_bookname(book_name)
        # print("book-", bookname)

        if bookname in Library.__books.keys():
            Library.__books[bookname] += 1
        else:
            Library.__books[bookname] = 1

    def _is_book_available(self, book_name):

        if book_name in self.__books:
            return self._book_count(book_name)

        return False

    def _book_count(self, book_name):
        return self.__books[book_name]

    def _check_user_have_book(self, username, book_name):
        if book_name in self.__records[username]:
            return True
        return False

    def borrow_book(self, username, book_name):

        if not self._is_book_available(book_name):
            return print(f"Book {book_name} is not present in the Library.")

        else:
            if self._is_book_available(book_name) == 0:
                print(f"{book_name} is already borrowed by someone.")

            elif self._is_book_available(book_name) > 0:  # unnecessary > 0

                if self._check_user_have_book(username, book_name):
                    return print(
                        f"{username} already have this book {book_name}"
                        )

                self.__records[username].add(book_name)
                self.__books[book_name] -= 1
                return print(
                    f"Book {book_name} Borrowed by {username} sucessfully."
                    )

    def return_book(self, username, book_name):

        user_borrowed_book = self.__records[username]

        if (
            book_name in self.__books.keys()
            and
            book_name in user_borrowed_book
        ):
            self.__books[book_name] += 1
            self.__records[username].remove(book_name)
            print(f"Book {book_name} returned sucessfully")

        elif book_name not in self.__books.keys():
            return print(f"Book {book_name} does not belongs to us.")

    def search_books(self, book_name):
        if book_name in self.__books.keys():
            return True

        print(f"{book_name} is not present in Library.")

    def add_member(self, username):
        if username not in self.__records.keys():
            self.__records[username] = set()

    def specific_user_book(self, username):
        # print("=>", self.__records[username], len(self.__records[username]))
        if len(self.__records[username]):
            return ", ".join(self.__records[username])
        return False


class Member(Library):

    def __init__(self, username=""):
        self.username = username

    def add_member(self, username):
        self.username = username
        super().add_member(username)

    def my_books(self):
        if super().specific_user_book(self.username):
            return print(super().specific_user_book(self.username))
        print("No Books")


def create_member(username):
    lib_instance = Library()
    user = Member()

    user.add_member(username)

    # lib_instance.get_books()
    lib_instance.add_book("Gandhi")
    lib_instance.add_book("saras")
    lib_instance.get_books()

    user.borrow_book(username, "Gandhi")
    user.borrow_book(username, "saras")
    user.my_books()
    lib_instance.get_books()
    user.return_book(username, "Gandhi")


try:
    username = input("Enter username to create member -")
    create_member(username)


except Exception as e:
    print(f"Error: {e}")
