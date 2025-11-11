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