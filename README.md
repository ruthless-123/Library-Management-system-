# 📚 Library Management System

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Code style: PEP 8](https://img.shields.io/badge/code%20style-PEP%208-green.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

A comprehensive Python-based Library Management System designed to efficiently manage books, members, and loans with a user-friendly CLI interface.

[Quick Start](#-quick-start) • [Features](#-features) • [Installation](#-installation--setup) • [Usage](#-usage) • [Architecture](#-architecture) • [Contributing](#-contributing)

</div>

---

## 📋 License & Tech Stack

### 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 ruthless-123

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

### 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Language** | Python 3.7+ |
| **Architecture** | MVC (Model-View-Controller) |
| **Design Pattern** | Service Layer Pattern |
| **Data Storage** | In-Memory (Dictionaries & Lists) |
| **UI** | Command Line Interface (CLI) |
| **Error Handling** | Custom Exception Classes |
| **Documentation** | Docstrings (PEP 257) |
| **Code Style** | PEP 8 Compliant |
| **Dependencies** | None (Standard Library Only) |

---

## 🎯 Project Overview

The **Library Management System** is a well-architected Python application that demonstrates professional software development practices. It provides a complete solution for managing library operations including book cataloging, member registration, book borrowing/returning, and loan tracking.

### Why This Project?
- ✅ **Educational**: Learn clean code architecture and design patterns
- ✅ **Practical**: Real-world library management scenario
- ✅ **Scalable**: Easy to extend with database integration
- ✅ **Professional**: Production-ready code with error handling
- ✅ **Well-Documented**: Comprehensive documentation and flowcharts

---

## ✨ Features

### 1. 📖 **Add Book** 
**Flowchart**: `_01_add_book.svg`

Add new books to the library with detailed information.

- **Inputs**: Book ID, Title, Author
- **Processing**: Creates Book object, stores in dictionary
- **Output**: Confirmation message
- **Data Stored**: 
  - `book_id`: Unique identifier
  - `title`: Book title
  - `author`: Author name
  - `available`: Auto-set to `True`

**Example:**
```
Book ID: B001
Title: Python Programming
Author: Guido van Rossum
✅ Book added: Python Programming
```

---

### 2. 👥 **Register Member**
**Flowchart**: `_02_register_member.svg`

Register new members to the library system.

- **Inputs**: Member ID, Name, Email
- **Processing**: Creates Member object, stores in dictionary
- **Output**: Confirmation message
- **Data Stored**:
  - `member_id`: Unique identifier
  - `name`: Full name
  - `email`: Contact email

**Example:**
```
Member ID: M001
Name: John Doe
Email: john@example.com
✅ Member registered: John Doe
```

---

### 3. 📤 **Borrow Book**
**Flowchart**: `_03_borrow_book.svg`

Allow members to borrow available books.

- **Inputs**: Book ID, Member ID
- **Validation**:
  - ✅ Book exists in library
  - ✅ Member is registered
  - ✅ Book is currently available
- **Processing**:
  - Mark book as borrowed (`available = False`)
  - Generate Loan ID (auto-incremented: L001, L002, ...)
  - Create Loan record with timestamp
- **Error Handling**:
  - ❌ `BookNotFoundError`: Book doesn't exist
  - ❌ `MemberNotFoundError`: Member not registered
  - ❌ `BookUnavailableError`: Book already borrowed
- **Output**: Success message or error message

**Example Success:**
```
Book ID: B001
Member ID: M001
✅ John Doe borrowed Python Programming
```

**Example Error:**
```
❌ Error: Book is already borrowed.
```

---

### 4. 📥 **Return Book**
**Flowchart**: `_04_return_book.svg`

Process book returns from members.

- **Inputs**: Loan ID
- **Processing**:
  - Find the loan record
  - Mark book as available (`available = True`)
  - Close the loan (`is_active = False`)
  - Record return date with timestamp
- **Error Handling**:
  - ❌ `LoanNotFoundError`: Loan ID doesn't exist
- **Output**: Success message

**Example:**
```
Loan ID: L001
✅ John Doe returned Python Programming
```

---

### 5. 📚 **View Books**
**Flowchart**: `_05_view_book.svg`

Display all books in the library with their status.

- **Processing**:
  - Retrieve all books
  - Check availability status for each book
  - Format and display information
- **Output Format**: `[Book ID] - [Title] by [Author] [Status]`
- **Status Options**:
  - 🟢 Available (not borrowed)
  - 🔴 Borrowed (currently checked out)

**Example Output:**
```
Books:
  B001 - Python Programming by Guido van Rossum [Available]
  B002 - Clean Code by Robert C. Martin [Borrowed]
  B003 - Design Patterns by Gang of Four [Available]
```

---

### 6. 👤 **View Members**
**Flowchart**: `_06_view_member.svg`

Display all registered library members.

- **Processing**:
  - Retrieve all members
  - Format member information
  - Display in table-like format
- **Output Format**: `[Member ID] - [Name] ([Email])`

**Example Output:**
```
Members:
  M001 - John Doe (john@example.com)
  M002 - Jane Smith (jane@example.com)
  M003 - Bob Johnson (bob@example.com)
```

---

### 7. 📋 **View Loans**
**Flowchart**: `_07_view_loan.svg`

Display all loan transactions (active and closed).

- **Processing**:
  - Retrieve all loans
  - Check loan status (active/closed)
  - Format loan information
  - Display in chronological order
- **Output Format**: `[Loan ID] - [Member Name] borrowed [Book Title] [Status]`
- **Status Options**:
  - 🟢 Active (book not yet returned)
  - 🔴 Closed (book has been returned)

**Example Output:**
```
Loans:
  L001 - John Doe borrowed Python Programming [Active]
  L002 - Jane Smith borrowed Clean Code [Closed]
  L003 - Bob Johnson borrowed Design Patterns [Active]
```

---

### 8. 🚪 **Exit**
**Flowchart**: `_08_exit.svg`

Gracefully exit the application.

- **Processing**:
  - Display closing message
  - Break from main loop
  - Terminate program
- **Output**: Program closed message

**Example:**
```
👋 Program closed.
```

---

## 🏗️ Architecture

### Project Structure
```
Library-Management-System/
│
├── 📄 main.py                      # Entry point & CLI interface
├── 📄 library_service.py           # Business logic layer (Service)
├── 📄 models.py                    # Data models (Model)
├── 📄 exceptions.py                # Custom exception classes
├── 📄 requirements.txt             # Python dependencies
├── 📄 README.md                    # This file
│
└── 📁 flowcharts/                  # Process flow diagrams (SVG)
    ├── _01_add_book.svg
    ├── _02_register_member.svg
    ├── _03_borrow_book.svg
    ├── _04_return_book.svg
    ├── _05_view_book.svg
    ├── _06_view_member.svg
    ├── _07_view_loan.svg
    └── _08_exit.svg
```

### Design Pattern: MVC Architecture

```
┌──────────────────────────────────────────────────────┐
│                    CLI Interface                     │
│                    (main.py)                         │
│  - Display Menu                                      │
│  - Get User Input                                    │
│  - Handle User Interactions                          │
└──────────────────┬───────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────┐
│              Service Layer                           │
│            (library_service.py)                      │
│  - Business Logic                                    │
│  - Validation & Error Handling                       │
│  - Data Orchestration                                │
└──────────────────┬───────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────┐
│              Data Models                             │
│                (models.py)                           │
│  - Book                                              │
│  - Member                                            │
│  - Loan                                              │
└──────────────────┬───────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────┐
│           In-Memory Data Storage                     │
│  - Books Dictionary {book_id: Book}                  │
│  - Members Dictionary {member_id: Member}           │
│  - Loans List [Loan, Loan, ...]                      │
└──────────────────────────────────────────────────────┘
```

### Class Hierarchy

#### **Book Class** (models.py)
```python
class Book:
    Attributes:
        - book_id: str          # Unique identifier
        - title: str            # Book title
        - author: str           # Author name
        - available: bool       # Availability status (default: True)
    
    Methods:
        - borrow()              # Mark as borrowed
        - return_book()         # Mark as returned
        - __str__()             # String representation
```

#### **Member Class** (models.py)
```python
class Member:
    Attributes:
        - member_id: str        # Unique identifier
        - name: str             # Member name
        - email: str            # Email address
    
    Methods:
        - __str__()             # String representation
```

#### **Loan Class** (models.py)
```python
class Loan:
    Attributes:
        - loan_id: str              # Unique identifier (L001, L002, ...)
        - book: Book                # Reference to borrowed book
        - member: Member            # Reference to borrowing member
        - borrow_date: datetime     # When book was borrowed
        - return_date: datetime     # When book was returned (or None)
        - is_active: bool           # Loan status (default: True)
    
    Methods:
        - close_loan()              # Mark loan as closed/returned
        - __str__()                 # String representation
```

#### **LibraryService Class** (library_service.py)
```python
class LibraryService:
    Private Attributes:
        - _books: Dict              # Dictionary of books
        - _members: Dict            # Dictionary of members
        - _loans: List              # List of loans
        - _loan_counter: int        # Auto-increment counter
    
    Book Operations:
        - add_book(book_id, title, author) → Book
        - view_books() → List[Book]
    
    Member Operations:
        - register_member(member_id, name, email) → Member
        - view_members() → List[Member]
    
    Loan Operations:
        - borrow_book(book_id, member_id) → Loan
        - return_book(loan_id) → Loan
        - view_loans() → List[Loan]
```

### Exception Hierarchy

```
Exception
    └── LibraryException (Base)
        ├── BookNotFoundError
        ├── MemberNotFoundError
        ├── BookUnavailableError
        └── LoanNotFoundError
```

---

## 📦 Installation & Setup

### Prerequisites
- **Python**: 3.7 or higher
- **Git**: For cloning the repository
- **Operating System**: Windows, macOS, or Linux

### Step 1: Clone the Repository
```bash
git clone https://github.com/ruthless-123/Library-Management-system-.git
cd Library-Management-system-
```

### Step 2: Verify Python Installation
```bash
python --version
# or
python3 --version
```

### Step 3: Install Dependencies (Optional)
```bash
pip install -r requirements.txt
```
*Note: This project has no external dependencies. All modules use Python Standard Library.*

### Step 4: Run the Application
```bash
python main.py
```

---

## 🚀 Usage

### Starting the Application
```bash
$ python main.py

🎉 Welcome to Library Management System! 🎉

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

Enter your choice (1-8): 
```

### Complete Workflow Example

#### Step 1: Add Books
```
Enter your choice (1-8): 1

--- Add Book ---
Enter Book ID: B001
Enter Book Title: Python Programming
Enter Book Author: Guido van Rossum
✅ Book added: Python Programming
```

#### Step 2: Register Members
```
Enter your choice (1-8): 2

--- Register Member ---
Enter Member ID: M001
Enter Member Name: John Doe
Enter Member Email: john@example.com
✅ Member registered: John Doe
```

#### Step 3: View All Books
```
Enter your choice (1-8): 5

--- View Books ---

Books:
  B001 - Python Programming by Guido van Rossum [Available]
```

#### Step 4: Borrow a Book
```
Enter your choice (1-8): 3

--- Borrow Book ---
Enter Book ID: B001
Enter Member ID: M001
✅ John Doe borrowed Python Programming
```

#### Step 5: View Loans
```
Enter your choice (1-8): 7

--- View Loans ---

Loans:
  L001 - John Doe borrowed Python Programming [Active]
```

#### Step 6: Return the Book
```
Enter your choice (1-8): 4

--- Return Book ---
Enter Loan ID: L001
✅ John Doe returned Python Programming
```

#### Step 7: Verify Book Status
```
Enter your choice (1-8): 5

--- View Books ---

Books:
  B001 - Python Programming by Guido van Rossum [Available]
```

#### Step 8: Exit Program
```
Enter your choice (1-8): 8

👋 Program closed.
```

---

## 🛡️ Error Handling

The system implements comprehensive error handling with custom exceptions:

### Exception Types

#### 1. **BookNotFoundError**
- **When**: Trying to borrow a non-existent book
- **Message**: "Book not found."
- **Example**:
```
Enter Book ID: B999
❌ Error: Book not found.
```

#### 2. **MemberNotFoundError**
- **When**: Trying to use an unregistered member ID
- **Message**: "Member not found."
- **Example**:
```
Enter Member ID: M999
❌ Error: Member not found.
```

#### 3. **BookUnavailableError**
- **When**: Attempting to borrow an already borrowed book
- **Message**: "Book is already borrowed."
- **Example**:
```
Enter Book ID: B001
Enter Member ID: M002
❌ Error: Book is already borrowed.
```

#### 4. **LoanNotFoundError**
- **When**: Trying to return a non-existent loan
- **Message**: "Loan not found."
- **Example**:
```
Enter Loan ID: L999
❌ Error: Loan not found.
```

#### 5. **Input Validation Errors**
- **When**: User enters empty or invalid fields
- **Message**: "Error: All fields are required."
- **Example**:
```
Enter Book ID: [blank]
❌ Error: All fields are required.
```

### Error Flow Diagram
```
User Input
    │
    ▼
Input Validation
    │
    ├─ Empty/Invalid ──→ ❌ Validation Error
    │
    ▼ Valid
Business Logic
    │
    ├─ Book Not Found ──→ ❌ BookNotFoundError
    ├─ Member Not Found ──→ ❌ MemberNotFoundError
    ├─ Book Unavailable ──→ ❌ BookUnavailableError
    ├─ Loan Not Found ──→ ❌ LoanNotFoundError
    │
    ▼ Success
Execute Operation
    │
    ▼
✅ Success Message
```

---

## 📊 Data Flow Diagrams

### Borrow Book Flow
```
┌─────────────────────────┐
│   Member Input IDs      │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│   Lookup Book           │
└──────────┬──────────────┘
           │
      ┌────┴─────┐
      │           │
     NO          YES
      │           │
      ▼           ▼
    ❌ Error   Continue
    Book      │
    Not       ▼
    Found   Lookup Member
            │
        ┌───┴─────┐
        │          │
       NO         YES
        │          │
        ▼          ▼
       ❌Error   Continue
       Member   │
       Not      ▼
       Found  Check Availability
             │
         ┌───┴─────┐
         │          │
        NO         YES
         │          │
         ▼          ▼
        ❌Error   ✅ Create Loan
        Not      Mark Book Borrowed
        Available Store Loan Record
                  │
                  ▼
              ✅ Success
```

### Return Book Flow
```
┌─────────────────────────┐
│   Member Input Loan ID  │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│   Lookup Loan           │
└──────────┬──────────────┘
           │
      ┌────┴─────┐
      │           │
     NO          YES
      │           │
      ▼           ▼
    ❌ Error   Continue
    Loan      │
    Not       ▼
    Found   Mark Book Available
            Close Loan
            Record Return Date
            │
            ▼
        ✅ Success
```

---

## 🔄 Data Persistence

### Current Implementation
- **Storage Type**: In-Memory (RAM)
- **Scope**: Session-based (data cleared on exit)
- **Books**: Dictionary keyed by `book_id`
- **Members**: Dictionary keyed by `member_id`
- **Loans**: List maintaining insertion order

### Data Loss Notes
```
⚠️  IMPORTANT: Data is NOT persisted
    - When you exit the program (Option 8), all data is lost
    - Data exists only during the current session
    - Next program run will start with empty collections
```

---

## 🚀 Future Enhancements

The system is designed to be easily extended with the following features:

### Phase 2: Database Integration
- [ ] SQLite database for persistent storage
- [ ] SQL queries for books, members, loans
- [ ] Database migrations and versioning
- [ ] Data export/import functionality

### Phase 3: Advanced Features
- [ ] **Due Date System**: Set return deadlines
- [ ] **Fine/Penalty System**: Calculate late fees
- [ ] **Search & Filter**: Find books by title, author
- [ ] **Book Reservations**: Queue system for popular books
- [ ] **Member Activity Log**: Track member borrowing history
- [ ] **Multiple Copies**: Support multiple copies of same book

### Phase 4: User Experience
- [ ] **User Authentication**: Login system for members
- [ ] **Admin Panel**: Dedicated admin interface
- [ ] **Web Interface**: Flask/Django web application
- [ ] **Mobile App**: Mobile-friendly interface
- [ ] **Email Notifications**: Remind members of due dates

### Phase 5: Enterprise Features
- [ ] **Multi-branch Support**: Manage multiple libraries
- [ ] **Analytics Dashboard**: Reports and statistics
- [ ] **Integration APIs**: RESTful API endpoints
- [ ] **Audit Trail**: Track all system changes
- [ ] **Role-based Access**: Different user permissions

---

## 📝 Code Quality

### Code Standards
- ✅ **PEP 8 Compliant**: Follows Python style guide
- ✅ **Docstrings**: Comprehensive documentation (PEP 257)
- ✅ **Type Hints**: Type annotations for clarity
- ✅ **Error Handling**: Custom exceptions and validation
- ✅ **Comments**: Clear, meaningful comments

### Best Practices Applied
- ✅ **Single Responsibility Principle**: Each class has one purpose
- ✅ **DRY (Don't Repeat Yourself)**: Reusable code components
- ✅ **SOLID Principles**: Well-structured object-oriented design
- ✅ **Separation of Concerns**: Model, Service, and View layers
- ✅ **Defensive Programming**: Input validation throughout

### Example: Well-Documented Method
```python
def borrow_book(self, book_id: str, member_id: str) -> Loan:
    """Borrow a book for a member.
    
    Args:
        book_id: ID of the book to borrow
        member_id: ID of the member borrowing
        
    Returns:
        Loan: The created loan object
        
    Raises:
        BookNotFoundError: If book not found
        MemberNotFoundError: If member not found
        BookUnavailableError: If book is not available
    """
    # Implementation with validation and error handling
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute
1. **Bug Reports**: Found a bug? Open an issue!
2. **Feature Requests**: Have a great idea? Let us know!
3. **Code Contributions**: Submit a pull request
4. **Documentation**: Improve or clarify docs
5. **Testing**: Write and share test cases

### Contribution Guidelines
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Library-Management-system-.git
cd Library-Management-system-

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Test your changes
python main.py
```

---

## 📚 Learning Resources

This project is perfect for learning:
- **Object-Oriented Programming (OOP)**: Classes, inheritance, encapsulation
- **Design Patterns**: MVC, Service Layer patterns
- **Exception Handling**: Custom exceptions, error management
- **CLI Development**: User input/output handling
- **Code Organization**: Project structure and architecture
- **Documentation**: Writing professional README files

### Related Topics to Explore
- Database integration (SQLite, PostgreSQL)
- Web frameworks (Flask, Django)
- Testing (unittest, pytest)
- API development (REST, FastAPI)
- Frontend development (HTML, CSS, JavaScript)

---

## 📞 Support & Contact

### Having Issues?
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the [Error Handling](#-error-handling) documentation
3. Open an [Issue on GitHub](https://github.com/ruthless-123/Library-Management-system-/issues)

### Get in Touch
- **Author**: ruthless-123
- **Email**: [Contact through GitHub](https://github.com/ruthless-123)
- **Repository**: [GitHub Link](https://github.com/ruthless-123/Library-Management-system-)

---

## 🎓 Troubleshooting

### Issue: "ModuleNotFoundError"
**Problem**: Python can't find the modules
**Solution**: Make sure you're running from the project root directory
```bash
cd Library-Management-system-
python main.py
```

### Issue: "No books found / No members found"
**Problem**: System shows empty lists
**Solution**: This is normal for a new session. Add books and members first using options 1 and 2.

### Issue: "Can't borrow a book"
**Problem**: Getting error messages
**Possible Causes**:
- Book ID doesn't exist → Use option 5 to see available books
- Member ID not registered → Use option 2 to register first
- Book already borrowed → Use option 5 to check availability

### Issue: "Python command not found"
**Problem**: `python` command not recognized
**Solution**: Try `python3` instead
```bash
python3 main.py
```

---

## 📊 Statistics

```
Project Metrics:
├── Total Files: 6
├── Lines of Code: ~650
├── Classes: 4
├── Methods: 20+
├── Exception Types: 4
├── Features: 8
├── Flowcharts: 8
└── Documentation: Comprehensive
```

---

## 📄 File Descriptions

| File | Purpose | Lines |
|------|---------|-------|
| `main.py` | CLI interface and user interactions | 180 |
| `library_service.py` | Business logic and service layer | 160 |
| `models.py` | Data model definitions | 130 |
| `exceptions.py` | Custom exception classes | 25 |
| `requirements.txt` | Project dependencies | 2 |
| `README.md` | This comprehensive guide | 600+ |

---

## 🏆 Acknowledgments

This project was created as a demonstration of:
- Clean code principles
- Professional software architecture
- Comprehensive documentation
- Best practices in Python development

---

## 🔒 Security Considerations

While this is an educational project, here are security considerations for production:

- [ ] Add input sanitization for all user inputs
- [ ] Implement user authentication and authorization
- [ ] Add role-based access control (RBAC)
- [ ] Encrypt sensitive data (if using database)
- [ ] Implement audit logging for all operations
- [ ] Add rate limiting for API endpoints
- [ ] Regular security audits and updates

---

## 📈 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-05-20 | Initial release with all 8 features |

---

<div align="center">

### Made with ❤️ by ruthless-123

**Give this project a ⭐ if you found it helpful!**

[Back to Top](#-library-management-system)

</div>
