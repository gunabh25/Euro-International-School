from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .selectors import (
    search_students,
    get_student_by_admission,
    get_subject_averages,
    get_top_student,
)

from .serializers import (
    StudentListSerializer,
    StudentDetailSerializer,
    CorrectionSerializer,
)

from .services import StudentService


class StudentListAPIView(APIView):
    """
    GET /api/students/?search=<text>
    """

    def get(self, request):
        search = request.query_params.get("search")

        students = search_students(search)

        serializer = StudentListSerializer(
            students,
            many=True,
        )

        return Response(serializer.data)


class StudentDetailAPIView(APIView):
    """
    GET /api/students/<admission_no>/
    """

    def get(self, request, admission_no):
        student = get_student_by_admission(admission_no)

        if student is None:
            return Response(
                {"error": "Student not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = StudentDetailSerializer(student)

        return Response(serializer.data)


class SummaryAPIView(APIView):
    """
    GET /api/summary/
    """

    def get(self, request):
        averages = get_subject_averages()

        top_student, total = get_top_student()

        data = StudentService.build_summary(
            averages,
            top_student,
            total,
        )

        return Response(data)


class CorrectionAPIView(APIView):
    """
    POST /api/marks/corrections/
    """

    def post(self, request):
        serializer = CorrectionSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            StudentService.apply_correction(
                admission_no=serializer.validated_data["admission_no"],
                subject=serializer.validated_data["subject"],
                marks=serializer.validated_data["marks"],
            )

        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"message": "Correction applied successfully."},
            status=status.HTTP_200_OK,
        )