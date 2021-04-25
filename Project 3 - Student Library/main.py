# Implement a student library system using OOPs where students can borrow a book from the list of books.
# Create a separate Library and Student class.
# Your program must be menu-driven.
# You are free to choose the methods and attributes of your choice to implement this functionality.

class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books Present in this library are: ")
        for book in self.books:
            print("\t * " + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Book is not available or has been issued to someone else. Please wait until the book available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this Book.")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
       
if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Python", "C Programming"])
    student = Student()
    #centralLibrary.displayAvailableBooks()

    while(True):
        WelcomeMsg = ''' ===== Welcome To Central Library ===== 
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add or Return a book
        4. Exit the Library
        '''
        print(WelcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thank You For Choosing Central Library.")
            exit()
        else:
            print("Invalid Choice")
        