from django.db.models import Avg, Sum

from .models import Student, Mark


def search_students(search_text=None):
    queryset = Student.objects.all()

    if search_text:
        queryset = queryset.filter(name__icontains=search_text)

    return queryset.order_by("name")


def get_student(admission_no):
    return Student.objects.prefetch_related(
        "marks"
    ).filter(
        admission_no=admission_no
    ).first()


def get_student_marks(student):
    return student.marks.all()


def get_subject_averages():
    return (
        Mark.objects.exclude(marks_obtained__isnull=True)
        .values("subject")
        .annotate(
            average=Avg("marks_obtained")
        )
        .order_by("subject")
    )


def get_top_student():
    students = Student.objects.prefetch_related("marks")

    best_student = None
    best_total = -1

    for student in students:

        total = (
            student.marks.exclude(
                marks_obtained__isnull=True
            ).aggregate(
                total=Sum("marks_obtained")
            )["total"]
            or 0
        )

        if total > best_total:
            best_total = total
            best_student = student

    return best_student, best_total