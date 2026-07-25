import csv
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db import transaction

from students.models import Student, Mark
from students.utils import (
    normalize_name,
    normalize_date,
    parse_marks,
)


class Command(BaseCommand):
    help = "Import students and marks from students_marks.csv"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.WARNING("Starting import..."))

        # Make the import re-runnable
        Mark.objects.all().delete()
        Student.objects.all().delete()

        csv_path = (
            Path(__file__)
            .resolve()
            .parents[4]
            / "data"
            / "students_marks.csv"
        )

        if not csv_path.exists():
            self.stdout.write(
                self.style.ERROR(
                    f"CSV file not found: {csv_path}"
                )
            )
            return

        duplicates = {}

        with open(csv_path, newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                admission_no = row["admission_no"].strip()
                subject = row["subject"].strip()

                marks = parse_marks(row["marks_obtained"])

                key = (admission_no, subject)

                if key not in duplicates:
                    duplicates[key] = row
                    continue

                existing = parse_marks(
                    duplicates[key]["marks_obtained"]
                )

                if existing is None:
                    if marks is not None:
                        duplicates[key] = row

                elif marks is not None and marks > existing:
                    duplicates[key] = row

        imported_students = {}

        for row in duplicates.values():

            admission_no = row["admission_no"].strip()

            if admission_no not in imported_students:

                student = Student.objects.create(
                    admission_no=admission_no,
                    name=normalize_name(
                        row["student_name"]
                    ),
                    student_class=row["class"].strip(),
                    section=row["section"].strip(),
                    date_of_birth=normalize_date(
                        row["date_of_birth"]
                    ),
                )

                imported_students[admission_no] = student

            student = imported_students[admission_no]

            Mark.objects.create(
                student=student,
                subject=row["subject"].strip(),
                marks_obtained=parse_marks(
                    row["marks_obtained"]
                ),
                max_marks=int(row["max_marks"]),
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Import completed successfully."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Students Imported : {Student.objects.count()}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Marks Imported : {Mark.objects.count()}"
            )
        )