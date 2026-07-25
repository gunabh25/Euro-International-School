from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView


class StudentListAPIView(APIView):
    def get(self, request):
        return Response({"message": "Student List"})


class StudentDetailAPIView(APIView):
    def get(self, request, admission_no):
        return Response({"message": admission_no})


class SummaryAPIView(APIView):
    def get(self, request):
        return Response({"message": "Summary"})


class CorrectionAPIView(APIView):
    def post(self, request):
        return Response({"message": "Correction"})
