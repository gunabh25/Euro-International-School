"""
Business logic for the Students application.
Views should call services instead of writing business logic directly.
"""


class StudentService:
    """Service layer for student-related operations."""

    @staticmethod
    def calculate_total(student):
        """
        Calculate total marks excluding absent subjects.
        """
        raise NotImplementedError("To be implemented.")

    @staticmethod
    def calculate_average(student):
        """
        Calculate average marks excluding absent subjects.
        """
        raise NotImplementedError("To be implemented.")

    @staticmethod
    def apply_correction(admission_no, subject, marks):
        """
        Apply a correction to a student's mark.
        """
        raise NotImplementedError("To be implemented.")