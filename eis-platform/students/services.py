from .selectors import (
    get_student_marks,
    get_subject_averages,
    get_top_student,
)

from .models import Mark


class StudentService:

    @staticmethod
    def calculate_total(student):

        total = 0

        for mark in get_student_marks(student):

            if mark.marks_obtained is not None:
                total += mark.marks_obtained

        return total

    @staticmethod
    def calculate_average(student):

        marks = []

        for mark in get_student_marks(student):

            if mark.marks_obtained is not None:
                marks.append(mark.marks_obtained)

        if not marks:
            return 0

        return round(sum(marks) / len(marks), 1)

    @staticmethod
    def get_summary():

        averages = []

        for subject in get_subject_averages():

            averages.append(
                {
                    "subject": subject["subject"],
                    "average": round(subject["average"], 1),
                }
            )

        top_student, total = get_top_student()

        return {
            "subject_averages": averages,
            "top_student": {
                "admission_no": top_student.admission_no,
                "name": top_student.name,
                "total": total,
            },
        }

    @staticmethod
    def apply_correction(
        admission_no,
        subject,
        marks,
    ):

        mark = Mark.objects.select_related(
            "student"
        ).get(
            student__admission_no=admission_no,
            subject=subject,
        )

        mark.marks_obtained = marks

        mark.save()

        return mark