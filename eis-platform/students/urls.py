from django.urls import path

from .views import (
    StudentListAPIView,
    StudentDetailAPIView,
    SummaryAPIView,
    CorrectionAPIView,
)

urlpatterns = [
    # Student List
    path(
        "students/",
        StudentListAPIView.as_view(),
        name="student-list",
    ),

    # Student Details
    path(
        "students/<str:admission_no>/",
        StudentDetailAPIView.as_view(),
        name="student-detail",
    ),

    # Summary
    path(
        "summary/",
        SummaryAPIView.as_view(),
        name="summary",
    ),

    # Apply Corrections
    path(
        "marks/corrections/",
        CorrectionAPIView.as_view(),
        name="mark-correction",
    ),
]