from django.http import HttpResponse
from .models import Topic, Course, Student, Order
from django.shortcuts import get_object_or_404


# Create your views here.
# Index view.
def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    course_list = Course.objects.all().order_by('-price')[:5]

    response = HttpResponse()
    heading1 = '<p>' + 'List of topics: ' + '</p>'
    response.write(heading1)

    print(top_list)
    for topic in top_list:
        para = '<p>' + str(topic.id) + ': ' + str(topic) + '</p>'
        response.write(para)

    heading2 = '<p>' + 'List of Courses: ' + '</p>'
    response.write(heading2)

    for course in course_list:
        if course.for_everyone:
            para = '<p>' + str(course.name) + ': ' + 'This course is for everyone' + str(course) + '</p>'
            response.write(para)
        else:
            para = '<p>' + str(course.name) + ': ' + 'This course is not for everyone' + '</p>'
            response.write(para)

    return response


# About view

def about(request):
    response = HttpResponse()
    heading3 = '<p>' + 'This is an E-learning Website! Search our Topics to find all available Courses.' + '<p>'
    response.write(heading3)
    return response


def details(request, id):
    response = HttpResponse()

    # topic = Topic.objects.get(id=id)
    topic = get_object_or_404(Topic, id=id)
    print(topic)
    heading4 = '<p>' + 'details page' + '<p>'
    response.write(heading4)
    response.write(topic.name)
    courses_list = Course.objects.filter(topic_id=topic.id)
    for course in courses_list:
        para = '<p>' + str(course.id) + ': ' + str(course.name) + '</p>'
        response.write(para)

    print(courses_list)

    return response
