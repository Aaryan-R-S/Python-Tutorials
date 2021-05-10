import random

class Library:
    def __init__(self, shelf, book):
        self.shelf = shelf
        self.code = random.randint(1000,9999)
        self.book = book
        self.name = None

    def __str__(self):  
        return f"[{self.shelf}] | (Id-{self.code}) : {self.book}"

    @staticmethod
    def displayBooks():
        for i in range(len(library)):
            print(library[i])
        
    @staticmethod
    def addBook(book):
        library.append(Library(f'Shelf-5', book))

    @staticmethod
    def lendBook(code, n):
            z = False
            for i in range(len(library)):
                if code == library[i].code:
                    library[i].name = n
                    lend.append(library[i])
                    library.remove(library[i])
                    print('Book Lent!')
                    z = True
                    break

            if z==False:
                for i in range(len(lend)):
                    if code == lend[i].code:
                        print(f"The Book, {lend[i].book}, is lented to {lend[i].name}")
                        z = True
            if z==False:
                print('No such Book Exist!')

    @staticmethod
    def returnBook(code):
            z = False
            for i in range(len(lend)):
                if code == lend[i].code:
                    lend[i].name = None
                    library.append(lend[i])
                    lend.remove(lend[i])
                    print('Book Returned!')
                    z = True
                    break

            if z==False:
                print('No such Book Exist!')

    @staticmethod
    def delBook(code):
            z = False
            for i in range(len(library)):
                if code == library[i].code:
                    library.remove(library[i])
                    print('Book Removed!')
                    z = True
                    break

            if z==False:
                print('No such Book Exist!')


a = Library('Shelf-1', 'Doraemon')
b = Library('Shelf-1', 'Motu Patlu')
c = Library('Shelf-2', 'Tom')
d = Library('Shelf-2', 'Shinchan')
e = Library('Shelf-3', 'Ninja')
f = Library('Shelf-3', 'Oggy') 
g = Library('Shelf-4', 'Pogo')
h = Library('Shelf-4', 'Mogli')

library = [a,b,c,d,e,f,g,h]
lend = []

print('\nWelcome to Gall.io Library!')

def func():
    while True:

        inp = input("\nPress 'show' : Display books, 'add' : Add book, 'del' : Remove book, 'lend': Lend book, 'return' : Return book & 'exit' : Exit Library\n ")

        if inp == 'show':
            print(f"\nAvailable Books({len(library)}) :")
            Library.displayBooks()

        if inp == 'add':
            book = input("\nType the Name of Book :\n ")
            Library.addBook(book)
            print('Book Added!')

        if inp == 'lend':
            n = input("\nType your Name :\n ")
            code = int(input("\nType the code of the book you want to lend :\n "))
            Library.lendBook(code, n)

        if inp == 'return':
            code = int(input("\nType the code of the book you want to return :\n "))
            Library.returnBook(code)

        if inp == 'del':
            code = int(input("\nType the code of the book you want to remove :\n "))
            Library.delBook(code)
        
        if inp == 'exit':
            # exit()
            break
        
func()

print('\nThanks for visiting us... Have a Nice Day!\n')