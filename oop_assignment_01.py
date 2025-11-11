class Book:
    def __init__(self,id, title, author, total_copies, available_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies
    
    def template(self):
        book = {
            'id':self.id,
            'title':self.title,
            'author':self.author,
            'total_copies':self.total_copies,
            'available_copies':self.available_copies
        }
        return book
    
class Member:
    def __init__(self,id, name, email, borrowed_books_list):
        self.id =id
        self.name = name 
        self.email = email
        self.borrowed_books_list = borrowed_books_list
        
    def template(self):
        member = {
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'borrowed_books_list':self.borrowed_books_list
            
        }
        return member