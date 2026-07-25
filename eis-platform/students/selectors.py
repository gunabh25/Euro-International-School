from django.db.models import Avg, Sum

from .models import Student, Mark


def search_students(search=None):
    """
    Return all students or search by name (case-insensitive).
    """

    queryset = Student.objects.all()

    if search:
        queryset = queryset.filter(
            name__icontains=search.strip()
        )

    return queryset.order_by("name")


def get_student_by_admission(admission_no):
    """
    Fetch one student with all marks.
    """

    return (
        Student.objects.prefetch_related("marks")
        .filter(admission_no=admission_no)
        .first()
    )


def get_subject_averages():
    """
    Average marks per subject excluding absents.
    """

    return (
        Mark.objects
        .exclude(marks_obtained__isnull=True)
        .values("subject")
        .annotate(
            average=Avg("marks_obtained")
        )
        .order_by("subject")
    )


def get_top_student():
    """
    Student with highest total marks.
    """

    best_student = None
    best_total = -1

    students = Student.objects.prefetch_related("marks")

    for student in students:

        total = (
            student.marks
            .exclude(marks_obtained__isnull=True)
            .aggregate(
                total=Sum("marks_obtained")
            )["total"]
            or 0
        )

        if total > best_total:
            best_total = total
            best_student = student

    return best_student, best_total