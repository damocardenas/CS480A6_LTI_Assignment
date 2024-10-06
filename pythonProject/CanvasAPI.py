# Import the Canvas Class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://canvas.instructure.com/"

# Canvas API key
API_KEY = "7~M88mG8tZFyPtE3EhaZC28Qt4DZxMWWDZUHATufzy2DHMyCaWFEvVuZAcyfzCcKVr"

# Initialize a Canvas object
# canvas = Canvas(API_URL, API_KEY)
#
# course = canvas.get_course(10367013)
# print(course.name)
#
# user = course.get_user(113770175)
# courses = user.get_courses()
# print(user.name)
# for c in courses:
#     print(c)
#
# users = course.get_users()
# for u in users:
#     print(u)
#     assignments = u.get_assignments(course)
#     for a in assignments:
#         print(a.name)

#####
canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(10367013)

users = course.get_users()
for u in users:
    print(f"Getting {u.name} Assignments")
    assignments = u.get_assignments(course)
    unsubmitted = u.get_assignments(course, bucket = "unsubmitted")
    for a in assignments:
        submit = True
        # print(f"Assignment - {a.name}")
        for un in unsubmitted:
            # print(f"UnSubmitted - {un.name}")
            if (a.name == un.name):
                submit = False
        if (submit):
            print(f"Submitted - {a.name}")
        else:
            print(f"Not Submitted - {a.name}")


    print(f"\n")

