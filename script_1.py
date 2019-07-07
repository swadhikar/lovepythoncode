import json


student_db = {50001: {'name': 'student_1', 'course': 'IT'}, 50002: {'name': 'student_2',
'course': 'Electronics'}, 50003: {'name': 'student_3', 'course': 'Computer Science'},
50004: {'name': 'student_4', 'course': 'Electronics'}}

""" json.dumps() function comes in handy to present nested data structures in a more elegant way """
formatted_text = json.dumps(student_db, indent=4)    # the function returns a formatted string that could later by printed!
print(formatted_text)

"""
Execution output:

/usr/bin/python3.6 /home/swadhi/Documents/lovepythoncode/script_1.py
{
    "50001": {
        "name": "student_1",
        "course": "IT"
    },
    "50002": {
        "name": "student_2",
        "course": "Electronics"
    },
    "50003": {
        "name": "student_3",
        "course": "Computer Science"
    },
    "50004": {
        "name": "student_4",
        "course": "Electronics"
    }
}

"""
