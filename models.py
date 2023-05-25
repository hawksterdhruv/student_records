
from datetime import date

import sqlalchemy as sa
from db import db


class Student(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String, nullable=False)
    family_name = sa.Column(sa.String, nullable=False)
    date_of_birth = sa.Column(sa.Date, nullable=False)
    email = sa.Column(sa.String, nullable=False)

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
        instance.date_of_birth = date.fromisoformat(raw_student['date_of_birth'])
        return instance


class Course(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    course_name = sa.Column(sa.String, nullable=False)


class Result(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    student_id = sa.ForeignKey(Student.id)
    course_id = sa.ForeignKey(Course.id)
    # Todo : Change grade to enum instead of String
    grade = sa.Column(sa.String, nullable=False)
