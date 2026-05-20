# Library Management System

A comprehensive Python-based Library Management System designed to manage books, members, and loans efficiently.

## Features

### 1. **Add Book** (Flowchart: `_01_add_book.svg`)
- Add new books to the library with unique IDs
- Store book details: ID, Title, Author
- Books are automatically marked as available when added

### 2. **Register Member** (Flowchart: `_02_register_member.svg`)
- Register new library members
- Store member information: ID, Name, Email
- Each member gets a unique identifier

### 3. **Borrow Book** (Flowchart: `_03_borrow_book.svg`)
- Members can borrow available books
- Validates book and member existence
- Checks book availability before lending
- Creates a loan record with auto-generated loan ID
- Marks book as unavailable when borrowed
- Error handling for:
  - Book not found
  - Member not found
  - Book already borrowed

### 4. **Return Book** (Flowchart: `_04_return_book.svg`)
- Members can return borrowed books
- Closes the loan record
- Marks the book as available again

### 5. **View Books** (Flowchart: `_05_view_book.svg`)
- Display all books in the library
- Shows book status (Available/Borrowed)
- Lists: ID, Title, Author, Status

### 6. **View Members** (Flowchart: `_06_view_member.svg`)
- Display all registered members
- Lists: ID, Name, Email

### 7. **View Loans** (Flowchart: `_07_view_loan.svg`)
- Display all loan transactions
- Shows loan status (Active/Closed)
- Lists: Loan ID, Member Name, Book Title, Status

### 8. **Exit** (Flowchart: `_08_exit.svg`)
- Gracefully exit the program

## Project Structure

```
Library-Management-System/
├── main.py                 # Entry point with CLI interface
├── library_service.py      # Core business logic (LibraryService class)
├── models.py              # Data models (Book, Member, Loan)
├── exceptions.py          # Custom exceptions
├── flowcharts/            # Process flow diagrams
│   ├── _01_add_book.svg
│   ├── _02_register_member.svg
│   ├── _03_borrow_book.svg
│   ├── _04_return_book.svg
│   ├── _05_view_book.svg
│   ├── _06_view_member.svg
│   ├── _07_view_loan.svg
│   └── _08_exit.svg
├── README.md              # This file
└── requirements.txt       # Python dependencies (if any)
```

## Class Hierarchy

### Models (`models.py`)

#### `Book`
- **Attributes:**
  - `book_id`: Unique identifier
  - `title`: Book title
  - `author`: Author name
  - `available`: Boolean flag (default: True)
- **Methods:**
  - `borrow()`: Mark as borrowed
  - `return_book()`: Mark as returned

#### `Member`
- **Attributes:**
  - `member_id`: Unique identifier
  - `name`: Member name
  - `email`: Email address

#### `Loan`
- **Attributes:**
  - `loan_id`: Unique identifier (L001, L002, ...)
  - `book`: Reference to Book object
  - `member`: Reference to Member object
  - `borrow_date`: Timestamp of borrow
  - `return_date`: Timestamp of return (if closed)
  - `is_active`: Boolean flag (True if active)
- **Methods:**
  - `close_loan()`: Mark as returned and close

### Service Layer (`library_service.py`)

#### `LibraryService`

**Book Operations:**
- `add_book(book_id, title, author) → Book`
- `view_books() → List[Book]`

**Member Operations:**
- `register_member(member_id, name, email) → Member`
- `view_members() → List[Member]`

**Loan Operations:**
- `borrow_book(book_id, member_id) → Loan`
- `return_book(loan_id) → Loan`
- `view_loans() → List[Loan]`

### Exceptions (`exceptions.py`)

- `LibraryException`: Base exception
- `BookNotFoundError`: When book ID doesn't exist
- `MemberNotFoundError`: When member ID doesn't exist
- `BookUnavailableError`: When book is already borrowed
- `LoanNotFoundError`: When loan ID doesn't exist

## Installation & Usage

### Prerequisites
- Python 3.7+
- No external dependencies required

### Running the System

```bash
# Clone the repository
git clone https://github.com/ruthless-123/Library-Management-system-.git
cd Library-Management-system-

# Run the program
python main.py
```

### Example Usage

```
==================================================
    LIBRARY MANAGEMENT SYSTEM
==================================================
1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. View Books
6. View Members
7. View Loans
8. Exit
==================================================

Enter your choice (1-8): 1

--- Add Book ---
Enter Book ID: B001
Enter Book Title: Python Programming
Enter Book Author: Guido van Rossum
✅ Book added: Python Programming

Enter your choice (1-8): 2

--- Register Member ---
Enter Member ID: M001
Enter Member Name: John Doe
Enter Member Email: john@example.com
✅ Member registered: John Doe

Enter your choice (1-8): 3

--- Borrow Book ---
Enter Book ID: B001
Enter Member ID: M001
✅ John Doe borrowed Python Programming

Enter your choice (1-8): 7

--- View Loans ---
Loans:
  L001 - John Doe borrowed Python Programming [Active]

Enter your choice (1-8): 8

👋 Program closed.
```

## Error Handling

The system includes comprehensive error handling:

1. **Book Not Found**: Occurs when trying to borrow a non-existent book
2. **Member Not Found**: Occurs when trying to borrow with invalid member ID
3. **Book Unavailable**: Occurs when trying to borrow an already borrowed book
4. **Loan Not Found**: Occurs when trying to return a non-existent loan
5. **Input Validation**: Checks for empty fields

## Process Flows

Each feature follows a detailed flowchart:

- **Add Book**: Input collection → Book creation → Dictionary storage → Success message
- **Register Member**: Input collection → Member creation → Dictionary storage → Success message
- **Borrow Book**: Input validation → Book lookup → Member lookup → Availability check → Loan creation → Success/Error message
- **Return Book**: Loan lookup → Book status update → Loan closure → Success message
- **View Books**: Collection retrieval → Status determination → Display formatting → List output
- **View Members**: Collection retrieval → Display formatting → List output
- **View Loans**: Collection retrieval → Status determination → Display formatting → List output
- **Exit**: Display message → Break loop → Program termination

## Data Storage

The system uses in-memory data structures:
- **Books**: Dictionary with book_id as key
- **Members**: Dictionary with member_id as key
- **Loans**: List of loan objects

Data is maintained during the session and cleared when the program exits.

## Future Enhancements

- Database integration (SQLite/PostgreSQL)
- Persistent data storage
- User authentication
- Fine/penalty system for late returns
- Book reservation feature
- Email notifications
- Search and filter functionality
- Admin panel
- Due date tracking

## Author

Created by: **ruthless-123**

## License

This project is open source and available under the MIT License.
