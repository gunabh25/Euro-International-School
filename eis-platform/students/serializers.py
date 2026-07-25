from rest_framework import serializers

from .models import Student, Mark


class MarkSerializer(serializers.ModelSerializer):

    class Meta:

        model = Mark

        fields = [
            "subject",
            "marks_obtained",
            "max_marks",
        ]


class StudentListSerializer(serializers.ModelSerializer):

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

        from .services import StudentService

        return StudentService.calculate_average(obj)


class StudentDetailSerializer(serializers.ModelSerializer):

    marks = MarkSerializer(many=True)

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

        from .services import StudentService

        return StudentService.calculate_total(obj)

    def get_average(self, obj):

        from .services import StudentService

        return StudentService.calculate_average(obj)


class CorrectionSerializer(serializers.Serializer):

    admission_no = serializers.CharField()

    subject = serializers.CharField()

    marks = serializers.IntegerField(min_value=0, max_value=100)