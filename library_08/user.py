class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"

    def get_book(self, author, book_name, days_to_return, library):
        for key, values in library.books_available.items():
                if key == author:
                    counter = -1
                    for item in values:
                        counter += 1
                        if item == book_name:
                            del library.books_available[key][counter]
                            library.rented_books[self.username] = {book_name: days_to_return}
                            self.books.append(book_name)
                            return f"{book_name} successfully rented for the next {days_to_return} days!"
        available_within = library.rented_books[self.username][book_name]
        return f'The book "{book_name}" is already rented and will be available in {available_within} days!'

    def return_book(self, author, book_name, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        library.books_available[author].append(book_name)
        del library.rented_books[self.username][book_name]
        self.books.remove(book_name)



    def info(self):
        # sort books rented by the user in ascending order
        self.sort()
        return ", ".join(self.books)


