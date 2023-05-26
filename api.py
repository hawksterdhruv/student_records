"""Apis for Student Records
- Currently also acts as the entry point for flask web server. 
Author : Dhruv Shah
"""
from typing import Dict, List
import re

from flask import Flask, Response, jsonify, render_template, request

from db import db
from models import Student, Course, Result


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


with app.app_context():
    db.create_all()


@app.route("/")
def home()->str:
    """Renders the index page for student records

    Returns:
        str: Rendered html for home/index page
    """
    return render_template("index.html")


##################################


@app.route("/api/v1/students")
def students() -> Response:
    """Gets List of students

    Returns:
        Response: returns student list in json form
    """
    students_results: List[Student] = Student.query.all()
    student_list: List[Dict] = [student.to_dict() for student in students_results]

    return jsonify({"data": student_list, "message": "SUCCESS"})


@app.route("/api/v1/student/<int:student_id>", methods=["GET"])
def get_student(student_id:int)->Response:
    """Gets the details for a particular student

    Args:
        student_id (int): id for the student record

    Returns:
        Response: return the student record in json form if found else error
    """
    student = Student.query.get_or_404(student_id)
    return jsonify({"data": student.to_dict(), "message": "SUCCESS"})


@app.route("/api/v1/student/", methods=["POST"])
def add_student() -> Response:
    """Allows you to add new students, requires a json input

    Returns:
        Response: returns json document for successful addition of student or error message
    """
    student_raw = request.get_json()
    error_message = validate_student_record(student_raw)
    if error_message:
        return jsonify({"data": None, "message": ", ".join(error_message)})

    new_student = Student().from_dict(student_raw)

    
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"data": new_student.to_dict(), "message": "SUCCESS"})

def validate_student_record(student_raw:Dict)->List:
    """Check student records and generates error messages

    Args:
        student_raw (Dict): student record from front end

    Returns:
        List: List of errors in student records
    """
    error_message = []
    if not student_raw['first_name'].strip():
        error_message.append( "Invalid First Name")
    if not student_raw['family_name'].strip():
        error_message.append("Invalid Family Name")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not student_raw['email'].strip() or not re.fullmatch(regex, student_raw['email'].strip()):
        error_message.append("Invalid Email")
    if not student_raw['date_of_birth'].strip():
        error_message.append("Invalid Date of Birth")
    return error_message


@app.route("/api/v1/student/<int:student_id>", methods=["DELETE"])
def delete_student(student_id: int) -> Response:
    """Allows you to delete students

    Args:
        student_id (int): id of the student to be deleted

    Returns:
        Response: Returns success if student deleted or Failure error message
    """
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"data": {}, "message": "SUCCESS"})


##################################


@app.route("/api/v1/courses")
def courses()->Response:
    """Gets List of courses

    Returns:
        Response: returns course list in json form
    """
    courses_results: List[Course] = Course.query.all()
    course_list: List[Dict] = [course.to_dict() for course in courses_results]
    return jsonify({"data": course_list, "message": "SUCCESS"})


@app.route("/api/v1/course/<int:course_id>", methods=["GET"])
def get_course(course_id:int)-> Response:
    """Gets the details for a particular course

    Args:
        course_id (int): id for the course record

    Returns:
        Response: return the course record in json form if found else error
    """
    course = Course.query.get_or_404(course_id)
    return jsonify({"data": course.to_dict(), "message": "SUCCESS"})


@app.route("/api/v1/course/", methods=["POST"])
def add_course()->Response:
    """Allows you to add new courses, requires a json input

    Returns:
        Response: returns json document for successful addition of course or error message
    """
    course_raw = request.get_json()
    if not course_raw['course_name'].strip():
        return jsonify({"data":None, "message":"Invalid Course Name"})
    new_course = Course().from_dict(course_raw)

    db.session.add(new_course)
    db.session.commit()
    return jsonify({"data": new_course.to_dict(), "message": "SUCCESS"})


@app.route("/api/v1/course/<int:course_id>", methods=["DELETE"])
def delete_course(course_id: int) -> Response:
    """Allows you to delete courses

    Args:
        course_id (int): id of the course to be deleted

    Returns:
        Response: Returns success if course deleted or Failure error message
    """
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({"data": {}, "message": "SUCCESS"})


##################################


@app.route("/api/v1/results")
def results():
    """Gets List of results

    Returns:
        str: returns result list in json form
    """
    results_results: List[Result] = Result.query.all()
    result_list: List[Dict] = [result.to_dict() for result in results_results]

    return jsonify({"data": result_list, "message": "SUCCESS"})


@app.route("/api/v1/result/<int:result_id>", methods=["GET"])
def get_result(result_id:int)->Response:
    """Gets the details for a particular result

    Args:
        result_id (int): id for the result record

    Returns:
        Response: return the result record in json form if found else error
    """
    result = Result.query.get_or_404(result_id)
    return jsonify({"data": result.to_dict(), "message": "SUCCESS"})


@app.route("/api/v1/result/", methods=["POST"])
def add_result() -> Response:
    """Allows you to add new results, requires a json input

    Returns:
        Response: returns json document for successful addition of result or error message
    """
    result_raw = request.get_json()
    new_result = Result().from_dict(result_raw)

    db.session.add(new_result)
    db.session.commit()
    return jsonify({"data": new_result.to_dict(), "message": "SUCCESS"})


@app.route("/api/v1/result/<int:result_id>", methods=["DELETE"])
def delete_result(result_id: int) -> Response:
    """Allows you to delete students

    Args:
        result_id (int): id of the student to be deleted

    Returns:
        Response: Returns success if student deleted or Failure error message
    """
    result = Result.query.get_or_404(result_id)
    db.session.delete(result)
    db.session.commit()
    return jsonify({"data": {}, "message": "SUCCESS"})


if __name__ == "__main__":
    app.run(debug=True)
