from django.http import HttpResponse
from django.shortcuts import render

from canvasapi import Canvas

# Canvas API URL
API_URL = "https://canvas.instructure.com/"

# Canvas API key
API_KEY = "7~M88mG8tZFyPtE3EhaZC28Qt4DZxMWWDZUHATufzy2DHMyCaWFEvVuZAcyfzCcKVr"

# Create your views here.
def index(request):
    header = "<h1> Welcome To Damyenn's Canvas LTI </h1>"
    userID = "<p> Welcome User: " + request.POST["custom_user_id"]
    courseID = " to the course: " + request.POST["custom_course_id"] + "</p>"

    courseUsers = "<p> Here are the users in course: " + request.POST["custom_course_id"] +" </p>"

    canvas = Canvas(API_URL, API_KEY)
    course = canvas.get_course(request.POST["custom_course_id"])
    users = course.get_users()

    listResponse = "<ul>"

    for user in users:
        listName = ""
        listAssignment = ""

        listName = f"<li> <i> {user.name} </i> <ul>"
        assignments = user.get_assignments(course)
        unsubmitted = user.get_assignments(course, bucket="unsubmitted")
        for assignment in assignments:
            submit = True
            for unsubmit in unsubmitted:
                if (assignment.name == unsubmit.name):
                    submit = False
            if (submit):
                listAssignment += f"<li> {assignment.name}: <strong> Submitted </strong> </li>"
            else:
                listAssignment += f"<li> {assignment.name}: <strong> Not Submitted </strong> </li>"

        listResponse += listName + listAssignment + "</ul>"

    listResponse += "</li> </ul>"

    return HttpResponse(header + userID + courseID + courseUsers + listResponse)