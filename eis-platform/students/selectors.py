"""
Selectors are responsible for reading data from the database.
No business logic should be written here.
"""

from .models import Student, Mark


def get_student_by_admission(admission_no):
    """
    Fetch a student using admission number.
    """
    return Student.objects.filter(
        admission_no=admission_no
    ).first()


def search_students(search_text):
    """
    Case-insensitive student search.
    """
    return Student.objects.filter(
        name__icontains=search_text
    )


def get_all_marks(student):
    """
    Return all marks for a student.
    """
    return Mark.objects.filter(student=student)