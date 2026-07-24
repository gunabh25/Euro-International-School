from django.db import models


class Student(models.Model):

    admission_no = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(max_length=100)

    student_class = models.CharField(max_length=10)

    section = models.CharField(max_length=5)

    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.admission_no} - {self.name}"


class Mark(models.Model):

    SUBJECT_CHOICES = [
        ("Maths", "Maths"),
        ("Science", "Science"),
        ("English", "English"),
        ("Hindi", "Hindi"),
        ("Social Science", "Social Science"),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="marks",
    )

    subject = models.CharField(
        max_length=30,
        choices=SUBJECT_CHOICES,
    )

    marks_obtained = models.IntegerField(
        null=True,
        blank=True,
    )

    max_marks = models.IntegerField(default=100)

    class Meta:

        unique_together = ("student", "subject")

        ordering = ["subject"]

    def __str__(self):
        return f"{self.student.name} - {self.subject}"