## Project Overview
This project demonstrates the transformation of a **Library Management System (LMS)** from a **procedural style** into an **Object-Oriented Programming (OOP)** design.  
It emphasizes **encapsulation, modularity, and reusability**, allowing users to manage books, members, and borrowing activities efficiently.  

The system includes features for:
- Adding and managing books and members  
- Borrowing and returning books  
- Displaying library information and transaction history  
- Handling invalid or exceptional scenarios gracefully  

## Project Structure
### library-management-oop/

#### README.md # Project documentation

#### procedural/
- lms.py # Original procedural implementation
- tester_ms.py # Comprehensive test suite for procedural version
#### oop/
- oop_assignment_01.py # Student's OOP implementation
- tester.py # Tests for the OOP version

## Design Overview
#### 1. **Book**
**Attributes**
- `book_id`: Unique ID of the book  
- `title`: Book title  
- `author`: Author name  
- `available`: Boolean status indicating if the book is available or borrowed  

**Key Methods**
- `borrow()`: Marks the book as borrowed (sets `available = False`)  
- `return_book()`: Marks the book as available again  
- `__str__()`: Displays formatted book information  

---

#### 2. **Member**
**Attributes**
- `member_id`: Unique ID of the member  
- `name`: Member name  
- `borrowed_books`: List of borrowed book IDs  

**Key Methods**
- `borrow_book(book)`: Allows the member to borrow a book (if available and within limit)  
- `return_book(book)`: Allows the member to return a borrowed book  
- `__str__()`: Displays formatted member information  

---

#### 3. **Library**
**Attributes**
- `books`: Dictionary or list containing all `Book` objects  
- `members`: Dictionary or list containing all `Member` objects  

**Key Methods**
- `add_book(book)`: Adds a new book to the system  
- `add_member(member)`: Registers a new member  
- `borrow_book(member_id, book_id)`: Handles the borrowing process  
- `return_book(member_id, book_id)`: Handles returning  
- `display_books()`: Lists all books with status  
- `display_members()`: Lists all members and their borrowed books  

---

## Testing

#### Basic Operations
- Adding books and members  
- Borrowing and returning books  
- Displaying information  

#### Edge Cases
- Borrowing unavailable books  
- Exceeding borrowing limit  
- Returning books not borrowed  
- Non-existent books or members  

---

### **How to Run Tests**
- Type 'python3 tester.py' in terminal or click run button.


