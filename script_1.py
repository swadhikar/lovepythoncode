import json


student_db = {50001: {'name': 'student_1', 'course': 'IT'}, 50002: {'name': 'student_2',
'course': 'Electronics'}, 50003: {'name': 'student_3', 'course': 'Computer Science'},
50004: {'name': 'student_4', 'course': 'Electronics'}}


formatted_text = json.dumps(student_db, indent=4)
print(formatted_text)
