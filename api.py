import json
from typing import Dict, List

from flask import Flask, jsonify, render_template, request

from db import db
from models import Student, Course, Result



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")


##################################


@app.route("/api/v1/students")
def students():

    students_results: List[Student] = Student.query.all()
    student_list: List[Dict] = [student.to_dict() for student in students_results]

    return jsonify({"data": student_list, "message": "SUCCESS"})


@app.route("/api/v1/student/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({"data": student.to_dict(), "message": "SUCCESS"})


@app.route("/api/v1/student/", methods=["POST"])
def add_student():
    student_raw = request.get_json()
    print(student_raw)
    new_student = Student().from_dict(student_raw)

    # Todo: Add validation here or check validation here
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"data": new_student.to_dict(), "message": "SUCCESS"})


@app.route("/api/v1/student/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"data": {}, "message": "SUCCESS"})


##################################


@app.route("/api/v1/courses")
def courses():
    courses_results: List[Course] = Course.query.all()
    course_list: List[Dict] = [course.to_dict() for course in courses_results]
    return jsonify({"data": course_list, "message": "SUCCESS"})


@app.route("/api/v1/course/<int:id>", methods=["GET"])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify({"data": course.to_dict(), "message": "SUCCESS"})


@app.route("/api/v1/course/", methods=["POST"])
def add_course():
    course_raw = request.get_json()
    new_course = Course().from_dict(course_raw)
    print(course_raw)

    # Todo: Add validation here or check validation here
    db.session.add(new_course)
    db.session.commit()
    return jsonify({"data": new_course.to_dict(), "message": "SUCCESS"})


@app.route("/api/v1/course/<int:id>", methods=["DELETE"])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({"data": {}, "message": "SUCCESS"})


##################################


@app.route("/api/v1/results")
def results():
    results_results: List[Result] = Result.query.all()
    result_list: List[Dict] = [result.to_dict() for result in results_results]

    return jsonify({"data": result_list, "message": "SUCCESS"})


@app.route("/api/v1/result/<int:id>", methods=["GET"])
def get_result(id):
    result = Result.query.get_or_404(id)
    return jsonify({"data": result.to_dict(), "message": "SUCCESS"})


@app.route("/api/v1/result/", methods=["POST"])
def add_result():
    result_raw = request.get_json()
    new_result = Result().from_dict(result_raw)

    # Todo: Add validation here or check validation here
    db.session.add(new_result)
    db.session.commit()
    return jsonify({"data": new_result.to_dict(), "message": "SUCCESS"})


@app.route("/api/v1/result/<int:id>", methods=["DELETE"])
def delete_result(id):
    result = Result.query.get_or_404(id)
    db.session.delete(result)
    db.session.commit()
    return jsonify({"data": {}, "message": "SUCCESS"})


if __name__ == "__main__":
    app.run(debug=True)
