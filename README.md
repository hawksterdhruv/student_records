# Student Records
Single page app to maintain students, courses, and their results 

## Talking points
1. Could have been done in React. 
2. Chose ORM, could have gone with SQL Builder
3. For Production 
   1. Would have used Gunicorn, or other WSGI server
   2. Would have used Swagger for api specs
   3. Would have used schema validators like marshmallow
   4. Would have separated serializes into its own module, marshmallow would have done it. 

## Known Issues
1. sqlite does not enforce foreign keys
2. ~~Delete not working~~
   1. Delete not cascading
3. ~~Validation not working~~
4. ~~Give page title~~
5. ~~Auto refresh page~~
6. Populate Tests
7. ~~Populate requirements.txt~~
8. ~~Add doc strings~~
9. Separate Views into separate module
10. ~~Date of birth 10 years check missing~~
11. ~~Success messages missing~~
12. Delete messages missing
13. Form clear
14. Grades in ENUM in the ORM
15. Add validation for duplicate results