class library:
    books=[]
    bookno=0
    unav=[]
    def addbook(self,l):
        library.books.append(l)
        library.bookno+=1
    def borrow(self,name,author):
        b=1
        for i in library.books:
            if(i==[name,author]):
                library.books.remove(i)
                library.unav.append(i)
                print("Borrow Successful")
                b=0
        if(b):
            print("BOOk unavailable")
        
    def show(self):
        print(f"{library.bookno} books are there")
        print(f"{len(library.books)} are currently available")
        for i in library.books:
            print(i)
    def ret(self,name,author):
        for i in library.unav:
            if(i==[name,author]):
                library.unav.remove(i)
                library.books.append(i)
a=library()
a.addbook(["ACOTAR","Sarah"])
a.addbook(["ACOMAF","Sarah"])
a.addbook(["Wimpy Kid","Jeff"])
a.addbook(["Animals","George"])
a.show()
a.borrow("ACOTAR","Sarah")
a.borrow("ACOWAR","Sarah")
a.show()
a.ret("ACOTAR","Sarah")
a.show()