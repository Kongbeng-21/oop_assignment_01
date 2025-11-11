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

class Library:
    def __init__(self,collections_of_books,members):
        self.collections_of_books = collections_of_books
        self.members = members
        
    def add_book(self,book_id, title, author, available_copies):
        book = {
            'id': book_id,
            'title': title,
            'author': author,
            'available_copies': available_copies,
            'total_copies': available_copies
        }
        books.append(book)
        print(f"Book '{title}' added successfully!")

    def add_member(self,member_id, name, email):
        member = {
            'id': member_id,
            'name': name,
            'email': email,
            'borrowed_books': []
        }
        members.append(member)
        print(f"Member '{name}' registered successfully!")
        
    def borrow_book(self,member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member:
            print("Error: Member not found!")
            return False
        
        if not book:
            print("Error: Book not found!")
            return False
        
        if book['available_copies'] <= 0:
            print("Error: No copies available!")
            return False
        
        if len(member['borrowed_books']) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
    
        # Process the borrowing
        book['available_copies'] -= 1
        member['borrowed_books'].append(book_id)
        
        transaction = {
            'member_id': member_id,
            'book_id': book_id,
            'member_name': member['name'],
            'book_title': book['title']
        }
        borrowed_books.append(transaction)
        
        print(f"{member['name']} borrowed '{book['title']}'")
        return True
    
    def return_book(self,member_id, book_id):
        """Process a book return transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member or not book:
            print("Error: Member or book not found!")
            return False
        
        if book_id not in member['borrowed_books']:
            print("Error: This member hasn't borrowed this book!")
            return False
        
        # Process the return
        book['available_copies'] += 1
        member['borrowed_books'].remove(book_id)
        
        # Remove from borrowed_books list
        for i, transaction in enumerate(borrowed_books):
            if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
                borrowed_books.pop(i)
                break
        
        print(f"{member['name']} returned '{book['title']}'")
        return True
    
    def display_available_books(self):
        """Display all books with available copies"""
        print("\n=== Available Books ===")
        for book in self.collections_of_books:
            if book['available_copies'] > 0:
                print(f"{book['title']} by {book['author']} - {book['available_copies']} copies available")

    def display_member_books(self,member_id):
        """Display books borrowed by a specific member"""
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        
        print(f"\n=== Books borrowed by {member['name']} ===")
        if not member['borrowed_books']:
            print("No books currently borrowed")
        else:
            for book_id in member['borrowed_books']:
                book = self.find_book(book_id)
                if book:
                    print(f"- {book['title']} by {book['author']}")

    def find_book(self,book_id):
            for book in self.collections_of_books:
                if book['id'] == book_id:
                    return book
            return None

    def find_member(self,member_id):
        for member in self.collections_of_books:
            if member['id'] == member_id:
                return member
        return None
    
books = []
members = []
borrowed_books = []