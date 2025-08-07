class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} [EBook, {self.file_size}KB]"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} [Print, {self.page_count} pages]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print(f"Added book: {book}")

    def list_books(self) -> None:
        if not self.books:
            print("The library has no books.")
            return
        
        print("Library Books:")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

if __name__ == "__main__":
    my_library = Library()
    
    ebook = EBook("Python Crash Course", "Eric Matthes", 5120)
    print_book = PrintBook("Clean Code", "Robert C. Martin", 464)
    
    my_library.add_book(ebook)
    my_library.add_book(print_book)
    
    my_library.list_books()