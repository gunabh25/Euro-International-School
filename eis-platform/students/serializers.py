from rest_framework import serializers

from .constants import SUBJECTS
from .models import Mark, Student
from .services import StudentService


class MarkSerializer(serializers.ModelSerializer):
    """
    Serializer for student marks.
    """

    marks = serializers.SerializerMethodField()

    class Meta:
        model = Mark
        fields = [
            "subject",
            "marks",
            "max_marks",
        ]

    def get_marks(self, obj):
        """
        Return None for absent students.
        DRF serializes None as null.
        """
        return obj.marks_obtained


class StudentListSerializer(serializers.ModelSerializer):
    """
    Serializer for student list endpoint.
    """

    average = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            "admission_no",
            "name",
            "student_class",
            "section",
            "date_of_birth",
            "average",
        ]

    def get_average(self, obj):
        return StudentService.calculate_average(obj)


class StudentDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for student detail endpoint.
    """

    marks = MarkSerializer(many=True, read_only=True)

    total = serializers.SerializerMethodField()

    average = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            "admission_no",
            "name",
            "student_class",
            "section",
            "date_of_birth",
            "marks",
            "total",
            "average",
        ]

    def get_total(self, obj):
        return StudentService.calculate_total(obj)

    def get_average(self, obj):
        return StudentService.calculate_average(obj)


class CorrectionSerializer(serializers.Serializer):
    """
    Validate correction payload.
    """

    admission_no = serializers.CharField(max_length=20)

    subject = serializers.CharField(max_length=30)

    marks = serializers.IntegerField()

    def validate_subject(self, value):

        if value not in SUBJECTS:
            raise serializers.ValidationError(
                "Invalid subject."
            )

        return value

    def validate_marks(self, value):

        if value < 0 or value > 100:
            raise serializers.ValidationError(
                "Marks must be between 0 and 100."
            )

        return value