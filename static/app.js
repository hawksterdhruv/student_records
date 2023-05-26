// STUDENT LIST
list_student = () => {
  $.get("api/v1/students", function (records) {
    console.log(records);
    $('[name="student_id"]').empty();
    $("#student_list-table tbody").empty();
    $.each(records["data"], function (idx, student) {
      $("#student_list-table tbody").append(
        "<tr>" +
          "<td>" +
          student["id"] +
          "</td>" +
          "<td>" +
          student["first_name"] +
          "</td>" +
          "<td>" +
          student["family_name"] +
          "</td>" +
          "<td>" +
          student["date_of_birth"] +
          "</td>" +
          "<td>" +
          student["email"] +
          "</td>" +
          "<td>" +
          "<button onclick=delete_student(" +
          student["id"] +
          ")>Delete Button</button>" +
          "</td>" +
          "</tr>"
      );
    });
    $.each(records["data"], function (idx, student) {
      $('[name="student_id"]').append("<option value=" + student["id"] + ">" + student["first_name"] + " " + student["family_name"] + "</option>");
    });
  });
};

// STUDENT ADD
add_student = (e) => {
  e.preventDefault();
  var student_values = $("#add_students form").serializeArray();
  var student_values_map = {};
  $.each(student_values, function (i, v) {
    student_values_map[v["name"]] = v["value"];
  });
  $.ajax({
    method: "POST",
    url: "api/v1/student",
    data: JSON.stringify(student_values_map),
    dataType: "json",
    contentType: "application/json",
  }).done(function (record) {
    if (record.message !== "SUCCESS") {
        $("#student-form-error .custom-message").html("<br>" + record.message);
        $("#student-form-error").show();
      }
    list_student();
    console.log(record);
  });
};

// DELETE STUDENT
delete_student = (student_id) => {
  $.ajax({
    method: "DELETE",
    url: "api/v1/student/" + student_id,
    dataType: "json",
  }).done(function (record) {

    list_student();
    console.log(record);
    // clear table and call student_list
  });
};

// COURSE  LIST
list_course = () => {
  $.get("api/v1/courses", function (records) {
    console.log(records);
    $('[name="course_id"]').empty();
    $("#courses_list-table tbody").empty();
    $.each(records["data"], function (idx, course) {
      $("#courses_list-table tbody").append(
        "<tr>" +
          "<td>" +
          course["id"] +
          "</td>" +
          "<td>" +
          course["course_name"] +
          "</td>" +
          "<td>" +
          "<button onclick=delete_course(" +
          course["id"] +
          ")>Delete Button</button>" +
          "</td>" +
          "</tr>"
      );
    });
    $.each(records["data"], function (idx, course) {
      $('[name="course_id"]').append("<option value=" + course["id"] + ">" + course["course_name"] + "</option>");
    });
  });
};

// COURSE ADD
add_course = (e) => {
  e.preventDefault();
  var course_values = $("#add_courses form").serializeArray();
  var course_values_map = {};
  $.each(course_values, function (i, v) {
    course_values_map[v["name"]] = v["value"];
  });
  $.ajax({
    method: "POST",
    url: "api/v1/course",
    data: JSON.stringify(course_values_map),
    dataType: "json",
    contentType: "application/json",
  }).done(function (record) {
    if (record.message !== "SUCCESS") {
      $("#course-form-error .custom-message").html("<br>" + record.message);
      $("#course-form-error").show();
    }
    list_course();
    console.log(record);
  });
  console.log("add course clicked");
};

// DELETE COURSE
delete_course = (course_id) => {
  $.ajax({
    method: "DELETE",
    url: "api/v1/course/" + course_id,
    dataType: "json",
  }).done(function (record) {
    list_course();
    console.log(record);
    // clear table and call course_list
  });
};

// RESULT LIST
list_result = () => {
  $.get("api/v1/results", function (records) {
    console.log(records);
    $("#results_list-table tbody").empty();
    $.each(records["data"], function (idx, result) {
      $("#results_list-table tbody").append(
        "<tr>" +
          "<td>" +
          result["id"] +
          "</td>" +
          "<td>" +
          result["student"]["first_name"] +
          " " +
          result["student"]["family_name"] +
          "</td>" +
          "<td>" +
          result["course"]["course_name"] +
          "</td>" +
          "<td>" +
          result["grade"] +
          "</td>" +
          "<td>" +
          "<button onclick=delete_result(" +
          result["id"] +
          ")>Delete Button</button>" +
          "</td>" +
          "</tr>"
      );
    });
  });
};

// RESULT ADD
add_result = (e) => {
  e.preventDefault();
  var result_values = $("#add_results form").serializeArray();
  var result_values_map = {};
  $.each(result_values, function (i, v) {
    result_values_map[v["name"]] = v["value"];
  });
  $.ajax({
    method: "POST",
    url: "api/v1/result",
    data: JSON.stringify(result_values_map),
    dataType: "json",
    contentType: "application/json",
  }).done(function (record) {
    list_result();
    console.log(record);
  });
  console.log("add result clicked");
};

// DELETE RESULT
delete_result = (result_id) => {
  $.ajax({
    method: "DELETE",
    url: "api/v1/result/" + result_id,
    dataType: "json",
    // contentType: 'application/json'
  }).done(function (record) {
    list_result();
    console.log(record);
    // clear table and call result_list
  });
};

$(function () {
  $("[data-hide]").on("click", function () {
    $(this)
      .closest("." + $(this).attr("data-hide"))
      .hide();
  });
});

$(document).ready(function () {
  list_course();
  list_result();
  list_student();
  $(".alert").hide();
});
