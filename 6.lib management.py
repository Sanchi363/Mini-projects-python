class library:
    def __init__(self):
        self.books=[]
        self.books_no=0
    def addbook(self,book):
        self.books.append(book)
        self.book_no=len(self.books)
    def show(self):
        print(f"The library has {self.books_no} books")
        print("The books are:")
        for i in self.books:
            print(i)
l1=library()
l1.addbook("A Court of Thorns and Roses")
l1.addbook("The diary of a Wimpy Kid")
l1.addbook("Early Indians")
l1.show()