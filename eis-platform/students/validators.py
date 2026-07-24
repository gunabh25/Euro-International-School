from .constants import SUBJECTS


def validate_subject(subject):

    return subject in SUBJECTS


def validate_marks(marks):

    if marks is None:
        return True

    if not isinstance(marks, int):
        return False

    return 0 <= marks <= 100


def validate_admission(admission):

    return admission.startswith("EIS-")