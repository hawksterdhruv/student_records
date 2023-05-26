 	


$( document ).ready(function() {
    console.log( "ready!" );
    // STUDENT LIST
    $.get('api/v1/students', function(records){
        console.log(records)
        $.each(records['data'], function(idx, student){
            $('#student_list-table tbody').append("<tr>"+
            "<td>"+student['id']+"</td>"+
            "<td>"+student['first_name']+"</td>"+
            "<td>"+student['family_name']+"</td>"+
            "<td>"+student['date_of_birth']+"</td>"+
            "<td>"+student['email']+"</td>"+
            "<td>"+"<button>Delete Button</button>"+"</td>"+
            "</tr>")
        });
        $.each(records['data'], function(idx, student){
            $('[name="student_id"]').append(
                "<option value="+student['id']+">"+student['first_name']+" "+student['family_name']+"</option>"
            )
        });
    })

    // STUDENT ADD
    $("#add_students form button").click(function(e){
        e.preventDefault();
        var student_values = $( "#add_students form" ).serializeArray();
        var student_values_map = {}
        $.each(student_values, function(i,v){student_values_map[v['name']] = v['value']})
        $.ajax({
            method: 'POST',
            url: 'api/v1/student',
            data: JSON.stringify(student_values_map),
            dataType: 'json',
            contentType: 'application/json'
        })
        console.log("add student clicked");
        
    })

    // COURSE  LIST
    $.get('api/v1/courses', function(records){
        console.log(records)
        $.each(records['data'], function(idx, course){
            $('#courses_list-table tbody').append("<tr>"+
            "<td>"+course['id']+"</td>"+
            "<td>"+course['course_name']+"</td>"+
            "<td>"+"<button>Delete Button</button>"+"</td>"+
            "</tr>")
        })
        $.each(records['data'], function(idx, course){
            $('[name="course_id"]').append(
                "<option value="+course['id']+">"+course['course_name']+"</option>"
            )
        })
    })

    // COURSE ADD
    $("#add_courses form button").click(function(e){
        e.preventDefault();
        var course_values = $( "#add_courses form" ).serializeArray();
        var course_values_map = {}
        $.each(course_values, function(i,v){course_values_map[v['name']] = v['value']})
        $.ajax({
            method: 'POST',
            url: 'api/v1/course',
            data: JSON.stringify(course_values_map),
            dataType: 'json',
            contentType: 'application/json'
        })
        console.log("add course clicked");  
    })

    // RESULT LIST
    $.get('api/v1/results', function(records){
        console.log(records)
        $.each(records['data'], function(idx, result){
            $('#results_list-table tbody').append("<tr>"+
            "<td>"+result['id']+"</td>"+
            "<td>"+result['student']['first_name']+" "+result['student']['family_name']+"</td>"+
            "<td>"+result['course']['course_name']+"</td>"+
            "<td>"+result['grade']+"</td>"+
            "<td>"+"<button>Delete Button</button>"+"</td>"+
            "</tr>")
        })
    })

    // RESULT ADD
    $("#add_results form button").click(function(e){
        e.preventDefault();
        var result_values = $( "#add_results form" ).serializeArray();
        var result_values_map = {}
        $.each(result_values, function(i,v){result_values_map[v['name']] = v['value']})
        $.ajax({
            method: 'POST',
            url: 'api/v1/result',
            data: JSON.stringify(result_values_map),
            dataType: 'json',
            contentType: 'application/json'
        })
        console.log("add result clicked");  
    })
});