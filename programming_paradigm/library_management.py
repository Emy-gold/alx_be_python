class Book:
    """Represents a book in the library system"""
    
    def __init__(self, title, author):
        """Initialize a book with title, author, and set it as available"""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute
    
    def check_out(self):
        """Mark the book as checked out"""
        if self._is_checked_out:
            return False  # Already checked out
        self._is_checked_out = True
        return True
    
    def return_book(self):
        """Mark the book as returned/available"""
        if not self._is_checked_out:
            return False  # Already available
        self._is_checked_out = False
        return True
    
    def is_available(self):
        """Check if the book is available"""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of books"""
    
    def __init__(self):
        """Initialize an empty library"""
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Add a book to the library"""
        if isinstance(book, Book):
            self._books.append(book)
    
    def find_book(self, title):
        """Find a book by its title (case-insensitive)"""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def check_out_book(self, title):
        """Check out a book by title"""
        book = self.find_book(title)
        if book and book.check_out():
            return True
        return False
    
    def return_book(self, title):
        """Return a book by title"""
        book = self.find_book(title)
        if book and book.return_book():
            return True
        return False
    
    def list_available_books(self):
        """Print all available books"""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available")
        else:
            for book in available_books:
                print(book)