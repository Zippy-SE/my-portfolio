import pytest
from student_registry import Student


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture
def student():
    return Student("Francisco", 15, "12th")


# ── __str__ ───────────────────────────────────────────────────────────────────

def test_str(student):
    assert str(student) == "Student 1: Name: Francisco, Age: 15, Grade: 12th"


# ── name getter / setter ──────────────────────────────────────────────────────

def test_name_getter(student):
    assert student.name == "Francisco"

def test_name_setter_valid(student):
    student.name = "Alice"
    assert student.name == "Alice"

def test_name_setter_too_short(student):
    student.name = "Al"
    assert student.name == "Francisco"  # unchanged

def test_name_setter_has_space(student):
    student.name = "Alice Smith"
    assert student.name == "Francisco"

def test_name_setter_special_char(student):
    student.name = "Al!ce"
    assert student.name == "Francisco"

def test_name_setter_not_title_case(student):
    student.name = "alice"
    assert student.name == "Francisco"

def test_name_setter_not_string(student):
    student.name = 123
    assert student.name == "Francisco"


# ── age getter / setter ───────────────────────────────────────────────────────

def test_age_getter(student):
    assert student.age == 15

def test_age_setter_valid(student):
    student.age = 14
    assert student.age == 14

def test_age_setter_too_young(student):
    student.age = 11
    assert student.age == 15  # unchanged

def test_age_setter_too_old(student):
    student.age = 18
    assert student.age == 15

def test_age_setter_not_int(student):
    student.age = "15"
    assert student.age == 15

def test_age_setter_float_rejected(student):
    student.age = 14.0
    assert student.age == 15


# ── grade getter / setter ─────────────────────────────────────────────────────

def test_grade_getter(student):
    assert student.grade == "12th"

def test_grade_setter_valid(student):
    student.grade = "9th"
    assert student.grade == "9th"

def test_grade_setter_invalid_format(student):
    student.grade = "12"
    assert student.grade == "12th"  # unchanged

def test_grade_setter_out_of_range(student):
    student.grade = "8th"
    assert student.grade == "12th"

def test_grade_setter_13th_rejected(student):
    student.grade = "13th"
    assert student.grade == "12th"


# ── study ─────────────────────────────────────────────────────────────────────

def test_study(student):
    assert student.study("Computer Science") == "Francisco is studying Computer Science"

def test_study_different_subject(student):
    assert student.study("Math") == "Francisco is studying Math"


# ── advance ───────────────────────────────────────────────────────────────────

def test_advance_default(student):
    result = student.advance()
    assert result == "Francisco has advanced to the 13th grade"
    assert student.grade == "13th"

def test_advance_multiple_years(student):
    result = student.advance(2)
    assert result == "Francisco has advanced to the 14th grade"
    assert student.grade == "14th"


# ── defaults ──────────────────────────────────────────────────────────────────

def test_default_age():
    s = Student("Maria")
    assert s.age == 13

def test_default_grade():
    s = Student("Maria")
    assert s.grade == "12th"
