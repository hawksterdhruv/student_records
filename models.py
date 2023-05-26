
from datetime import date

from db import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    family_name = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    email = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "family_name": self.family_name,
            "email": self.email,
            "date_of_birth": str(self.date_of_birth)
        }

    @classmethod
    def from_dict(cls, raw_student):
        instance = cls()
        instance.first_name = raw_student['first_name']
        instance.family_name = raw_student['family_name']
        instance.email = raw_student['email']
        instance.date_of_birth = date.fromisoformat(
            raw_student['date_of_birth'])
        return instance


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "course_name": self.course_name
        }

    @classmethod
    def from_dict(cls, raw_course):
        instance = cls()
        instance.course_name = raw_course['course_name']

        return instance


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.ForeignKey(Student.id), nullable=False)
    course_id = db.Column(db.ForeignKey(Course.id), nullable=False)
    # Todo : Change grade to enum instead of String
    grade = db.Column(db.String, nullable=False)
    student = db.relationship('Student')
    course = db.relationship('Course')

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "course_id": self.course_id,
            "grade": self.grade,
            "student": self.student.to_dict(),
            "course": self.course.to_dict()
        }

    @classmethod
    def from_dict(cls, raw_result):
        instance = cls()
        instance.student_id = raw_result['student_id']
        instance.course_id = raw_result['course_id']
        instance.grade = raw_result['grade']

        return instance
