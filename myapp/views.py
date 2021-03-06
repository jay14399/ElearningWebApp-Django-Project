from django.http import HttpResponse

from myapp.forms import InterestForm, OrderForm
from .models import Topic, Course, Student, Order
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render


# Create your views here.
# Index view.


def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'top_list': top_list})
    #  course_list = Course.objects.all().order_by('-price')[:5]

    #  response = HttpResponse()

    #  heading1 = '<p>' + 'List of topics: ' + '</p>'
    #  response.write(heading1)

    #  print(top_list)
    #  for topic in top_list:
    #   para = '<p>'+ str(topic.id) + ': ' + str(topic) + '</p>'
    #   response.write(para)

    #  heading2 = '<p>' + 'List of Courses: ' + '</p>'
    #  response.write(heading2)

    #  for course in course_list:
    #   if course.for_everyone:
    #    para = '<p>'+ str(course.name) + ': ' + 'This course is for everyone' + str(course) +'</p>'
    #    response.write(para)
    #   else:
    #    para = '<p>' + str(course.name) + ': ' + 'This course is not for everyone' + '</p>'
    #    response.write(para)

    # return response


# # About view

def about(request):
    return render(request, 'myapp/about.html')
    # ans 3,4: No need to use context variable because it is simple html text

    # response = HttpResponse()
    # heading3 = '<p>' + \
    #     'This is an E-learning Website! Search our Topics to find all available Courses.' + '<p>'
    # response.write(heading3)
    # return response


def details(request, id):
    topic = get_object_or_404(Topic, id=id)
    courses_list = Course.objects.filter(topic_id=topic.id)
    return render(request, 'myapp/detail.html', {'topic': topic, 'course_list': courses_list})

    # Yes, we have used context variable to pass the content of course list and topic in template

    # response = HttpResponse()

    # # topic = Topic.objects.get(id=id)
    # topic = get_object_or_404(Topic, id=id)
    # print(topic)
    # heading4 = '<p>' + 'details page' + '<p>'
    # response.write(heading4)
    # response.write(topic.name)
    # response.write('<br>'+'Topic Category: '+topic.category)
    # courses_list = Course.objects.filter(topic_id=topic.id)
    # for course in courses_list:
    #     para = '<p>' + str(course.id) + ': ' + str(course.name) + '</p>'
    #     response.write(para)

    # print(courses_list)

    # return response


def courses(request):
    courses_list = Course.objects.all().order_by("id")
    return render(request, 'myapp/courses.html', {'courses': courses_list})


def place_order(request):
    msg = ''
    course_list = Course.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.levels <= order.course.stages:
                order.save()
                msg = 'Your course has been ordered successfully.'
                if order.course.price > 150.00:
                    order.course.discount()
            else:
                msg = 'You exceeded the number of levels for this course.'
            return render(request, 'myapp/order_response.html', {'msg': msg})
    else:
        form = OrderForm()
    return render(request, 'myapp/place_order.html', {'form': form, 'msg': msg, 'course_list': course_list})


def course_detail(request, cour_id):
    course = get_object_or_404(Course, pk=cour_id)
    if request.method == 'POST':
        form = InterestForm(request.POST)
        # print(form.cleaned_data("interested"))
        if form.is_valid():
            # print(form.cleaned_data["interested"] == 1)
            if form.cleaned_data["interested"] == "1":
                course.interested = course.interested+1
                course.save()
                return redirect('/myapp/')
            else:
                return redirect('/myapp/')
        else:
            msg = 'There was an error in saving. Please try again'
            return redirect(request, 'myapp/interest_response.html', {'msg': msg})
    else:
        form = InterestForm()
        return render(request, 'myapp/course_detail.html', {'form': form, 'course': course})
