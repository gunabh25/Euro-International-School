from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .selectors import (
    search_students,
    get_student,
)

from .serializers import (
    StudentListSerializer,
    StudentDetailSerializer,
    CorrectionSerializer,
)

from .services import StudentService


class StudentListAPIView(APIView):

    def get(self, request):

        students = search_students(
            request.GET.get("search")
        )

        serializer = StudentListSerializer(
            students,
            many=True,
        )

        return Response(serializer.data)


class StudentDetailAPIView(APIView):

    def get(self, request, admission_no):

        student = get_student(admission_no)

        if not student:
            return Response(
                {"error": "Student not found"},
                status=404,
            )

        serializer = StudentDetailSerializer(
            student
        )

        return Response(serializer.data)


class SummaryAPIView(APIView):

    def get(self, request):

        return Response(
            StudentService.get_summary()
        )


class CorrectionAPIView(APIView):

    def post(self, request):

        serializer = CorrectionSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        StudentService.apply_correction(
            **serializer.validated_data
        )

        return Response(
            {
                "message": "Correction applied."
            },
            status=status.HTTP_200_OK,
        )