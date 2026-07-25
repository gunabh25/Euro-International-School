from django.urls import path

from .views import (
    StudentListAPIView,
    StudentDetailAPIView,
    SummaryAPIView,
    CorrectionAPIView,
)

urlpatterns = [
    path(
        "students/",
        StudentListAPIView.as_view(),
        name="student-list",
    ),

    path(
        "students/<str:admission_no>/",
        StudentDetailAPIView.as_view(),
        name="student-detail",
    ),

    path(
        "summary/",
        SummaryAPIView.as_view(),
        name="summary",
    ),

    path(
        "marks/corrections/",
        CorrectionAPIView.as_view(),
        name="correction",
    ),
]