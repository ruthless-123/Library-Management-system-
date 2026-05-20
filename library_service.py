"""LibraryService class for managing books, members, and loans.

Provides business logic for all library operations.
"""

from typing import Dict, List
from models import Book, Member, Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)


class LibraryService:
    """Service class for managing library operations."""
    
    def __init__(self):
        """Initialize the LibraryService with empty collections."""
        self._books: Dict[str, Book] = {}
        self._members: Dict[str, Member] = {}
        self._loans: List[Loan] = []
        self._loan_counter = 0
    
    # ===== BOOK MANAGEMENT =====
    
    def add_book(self, book_id: str, title: str, author: str) -> Book:
        """Add a new book to the library.
        
        Args:
            book_id: Unique book identifier
            title: Book title
            author: Book author
            
        Returns:
            Book: The created book object
        """
        book = Book(book_id, title, author)
        self._books[book.book_id] = book
        return book
    
    def view_books(self) -> List[Book]:
        """Get all books in the library.
        
        Returns:
            List[Book]: List of all books
        """
        return list(self._books.values())
    
    # ===== MEMBER MANAGEMENT =====
    
    def register_member(self, member_id: str, name: str, email: str) -> Member:
        """Register a new member to the library.
        
        Args:
            member_id: Unique member identifier
            name: Member name
            email: Member email
            
        Returns:
            Member: The created member object
        """
        member = Member(member_id, name, email)
        self._members[member.member_id] = member
        return member
    
    def view_members(self) -> List[Member]:
        """Get all members of the library.
        
        Returns:
            List[Member]: List of all members
        """
        return list(self._members.values())
    
    # ===== LOAN MANAGEMENT =====
    
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
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
        
        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")
        
        # Check book availability
        if not book.available:
            raise BookUnavailableError("Book is already borrowed.")
        
        # Mark book as borrowed and create loan
        book.borrow()
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)
        
        return loan
    
    def return_book(self, loan_id: str) -> Loan:
        """Return a borrowed book.
        
        Args:
            loan_id: ID of the loan
            
        Returns:
            Loan: The closed loan object
            
        Raises:
            LoanNotFoundError: If loan not found
        """
        # Find the loan
        loan = None
        for l in self._loans:
            if l.loan_id == loan_id:
                loan = l
                break
        
        if loan is None:
            raise LoanNotFoundError("Loan not found.")
        
        # Return the book
        loan.book.return_book()
        loan.close_loan()
        
        return loan
    
    def view_loans(self) -> List[Loan]:
        """Get all loans (active and closed).
        
        Returns:
            List[Loan]: List of all loans
        """
        return list(self._loans)
