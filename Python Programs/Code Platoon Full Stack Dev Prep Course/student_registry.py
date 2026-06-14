import re

VALID_GRADES = {"9th", "10th", "11th", "12th"}


class Student:
    def __init__(self, name, age=13, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade

    # ── name ──────────────────────────────────────────────────────────────────

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        # 3+ chars, no spaces or special characters, title case
        if (
            isinstance(new_name, str)
            and len(new_name) >= 3
            and re.fullmatch(r"[A-Za-z]+", new_name)
            and new_name == new_name.title()
        ):
            self._name = new_name

    # ── age ───────────────────────────────────────────────────────────────────

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 11 < new_age < 18:
            self._age = new_age

    # ── grade ─────────────────────────────────────────────────────────────────

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if new_grade in VALID_GRADES:
            self._grade = new_grade

    # ── dunder methods ────────────────────────────────────────────────────────

    def __str__(self):
        return f"Student 1: Name: {self._name}, Age: {self._age}, Grade: {self._grade}"

    # ── instance methods ──────────────────────────────────────────────────────

    def advance(self, years_advanced=1):
        current_num = int(self._grade.replace("th", ""))
        new_num = current_num + years_advanced
        new_grade = f"{new_num}th"
        self._grade = new_grade
        return f"{self._name} has advanced to the {new_grade} grade"

    def study(self, subject):
        return f"{self._name} is studying {subject}"


# ── Instances ─────────────────────────────────────────────────────────────────

s1 = Student("Francisco", 15, "12th")
s2 = Student("Maria", 14, "10th")
s3 = Student("James", 16, "11th")

for student in [s1, s2, s3]:
    print(student)
    print(f"  Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

print()
print(s1.study("Computer Science"))
print(s1.advance())
print(s2.advance(2))
