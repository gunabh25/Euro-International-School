from django.db import transaction

from .constants import SUBJECTS
from .models import Mark

from .selectors import (
    get_subject_averages,
    get_top_student,
)


class StudentService:

    @staticmethod
    def calculate_total(student):

        return sum(
            mark.marks_obtained
            for mark in student.marks.all()
            if mark.marks_obtained is not None
        )

    @staticmethod
    def calculate_average(student):

        marks = [
            mark.marks_obtained
            for mark in student.marks.all()
            if mark.marks_obtained is not None
        ]

        if not marks:
            return 0.0

        return round(sum(marks) / len(marks), 1)

    @staticmethod
    def build_summary():

        averages = []

        for item in get_subject_averages():

            averages.append(
                {
                    "subject": item["subject"],
                    "average": round(item["average"], 1),
                }
            )

        student, total = get_top_student()

        return {
            "subject_averages": averages,
            "top_student": {
                "admission_no": student.admission_no,
                "name": student.name,
                "total": total,
            },
        }

    @staticmethod
    @transaction.atomic
    def apply_correction(
        admission_no,
        subject,
        marks,
    ):

        if subject not in SUBJECTS:
            raise ValueError("Invalid subject")

        mark = (
            Mark.objects
            .select_related("student")
            .filter(
                student__admission_no=admission_no,
                subject=subject,
            )
            .first()
        )

        if not mark:
            raise ValueError(
                "Student or subject not found"
            )

        mark.marks_obtained = marks
        mark.save()

        return mark