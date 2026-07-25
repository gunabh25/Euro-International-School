from django.db import transaction

from .constants import SUBJECTS
from .models import Mark


class StudentService:
    """
    Business logic for students and marks.
    """

    @staticmethod
    def calculate_total(student):
        """
        Calculate total marks excluding absent subjects.
        """

        return sum(
            mark.marks_obtained
            for mark in student.marks.all()
            if mark.marks_obtained is not None
        )

    @staticmethod
    def calculate_average(student):
        """
        Calculate average excluding absent subjects.
        """

        marks = [
            mark.marks_obtained
            for mark in student.marks.all()
            if mark.marks_obtained is not None
        ]

        if not marks:
            return 0.0

        return round(sum(marks) / len(marks), 1)

    @staticmethod
    def get_student_marks(student):
        """
        Return marks in assignment format.
        """

        result = []

        for mark in student.marks.all():

            result.append(
                {
                    "subject": mark.subject,
                    "marks": mark.marks_obtained,
                    "max_marks": mark.max_marks,
                }
            )

        return result

    @staticmethod
    def build_student_response(student):
        """
        Build response for Student Detail API.
        """

        return {
            "admission_no": student.admission_no,
            "name": student.name,
            "class": student.student_class,
            "section": student.section,
            "dob": student.date_of_birth,
            "marks": StudentService.get_student_marks(student),
            "total": StudentService.calculate_total(student),
            "average": StudentService.calculate_average(student),
        }

    @staticmethod
    def build_summary(subject_averages, top_student, total):
        """
        Build Summary API response.
        """

        averages = []

        for item in subject_averages:

            averages.append(
                {
                    "subject": item["subject"],
                    "average": round(item["average"], 1),
                }
            )

        return {
            "subject_averages": averages,
            "top_student": {
                "admission_no": top_student.admission_no,
                "name": top_student.name,
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
        """
        Apply mark correction.
        """

        if subject not in SUBJECTS:
            raise ValueError("Invalid subject.")

        if not isinstance(marks, int):
            raise ValueError("Marks must be integer.")

        if marks < 0 or marks > 100:
            raise ValueError("Marks should be between 0 and 100.")

        mark = (
            Mark.objects
            .select_related("student")
            .filter(
                student__admission_no=admission_no,
                subject=subject,
            )
            .first()
        )

        if mark is None:
            raise ValueError(
                "Student or subject not found."
            )

        mark.marks_obtained = marks
        mark.save()

        return mark