"""Models for the Library Management System.

Defines the core data models:
- Book: Represents a book in the library
- Member: Represents a member of the library
- Loan: Represents a book loan transaction
"""

from datetime import datetime
from typing import Optional


class Book:
    """Represents a book in the library.
    
    Attributes:
        book_id (str): Unique identifier for the book
        title (str): Title of the book
        author (str): Author of the book
        available (bool): Whether the book is available for borrowing
    """
    
    def __init__(self, book_id: str, title: str, author: str):
        """Initialize a Book object.
        
        Args:
            book_id: Unique identifier
            title: Book title
            author: Book author
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self) -> None:
        """Mark the book as borrowed."""
        self.available = False
    
    def return_book(self) -> None:
        """Mark the book as returned."""
        self.available = True
    
    def __str__(self) -> str:
        """String representation of the book."""
        status = "Available" if self.available else "Borrowed"
        return f"{self.book_id} - {self.title} by {self.author} [{status}]"


class Member:
    """Represents a library member.
    
    Attributes:
        member_id (str): Unique identifier for the member
        name (str): Name of the member
        email (str): Email address of the member
    """
    
    def __init__(self, member_id: str, name: str, email: str):
        """Initialize a Member object.
        
        Args:
            member_id: Unique identifier
            name: Member name
            email: Member email address
        """
        self.member_id = member_id
        self.name = name
        self.email = email
    
    def __str__(self) -> str:
        """String representation of the member."""
        return f"{self.member_id} - {self.name} ({self.email})"


class Loan:
    """Represents a book loan transaction.
    
    Attributes:
        loan_id (str): Unique identifier for the loan
        book (Book): The book being loaned
        member (Member): The member borrowing the book
        borrow_date (datetime): Date when the book was borrowed
        return_date (Optional[datetime]): Date when the book was returned
        is_active (bool): Whether the loan is still active
    """
    
    def __init__(self, loan_id: str, book: Book, member: Member):
        """Initialize a Loan object.
        
        Args:
            loan_id: Unique identifier
            book: The book object
            member: The member object
        """
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.borrow_date = datetime.now()
        self.return_date: Optional[datetime] = None
        self.is_active = True
    
    def close_loan(self) -> None:
        """Mark the loan as closed (book returned)."""
        self.return_date = datetime.now()
        self.is_active = False
    
    def __str__(self) -> str:
        """String representation of the loan."""
        status = "Active" if self.is_active else "Closed"
        return f"{self.loan_id} - {self.member.name} borrowed {self.book.title} [{status}]"
