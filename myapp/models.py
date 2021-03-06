from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.core import serializers


class Topic(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, blank=True)

    def toJson(self):
      return serializers.serialize('json', [self])

    def __str__(self):
      return f"ID: {str(self.id)} Name: " + str(self.name) + "\n Category:" + str(self.category) + "\n"

    def get_category(self):
      return self.category


class Course(models.Model):
    topic = models.ForeignKey(Topic, related_name='courses',
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    for_everyone = models.BooleanField(default=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    interested = models.PositiveIntegerField(default=0)
    stages = models.PositiveIntegerField(default=3)

    def __str__(self):
        return 'Topic=' + self.topic.name + ' Name=' + self.name + ' Price=' + str(self.price) + ' For everyone=' + str(
            self.for_everyone) + ' Description=' + self.description

    def discount(self):
        return self.price - (0.10 * self.price); 


class Student(User):
    CITY_CHOICES = [('WS', 'Windsor'),
                    ('CG', 'Calgery'),
                    ('MR', 'Montreal'),
                    ('VC', 'Vancouver')]
    school = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='WS')
    interested_in = models.ManyToManyField(Topic)

    def __str__(self):
        return 'Name=' + self.username


class Order(models.Model):
    courses = models.ManyToManyField(Course)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    level = models.IntegerField(blank=True)
    order_status = [(0, 'Cancelled'), (1, 'Order Confirmed')]
    order_date = models.DateField(default=timezone.now)

    def total_cost(self):
        total = 0

        for course in self.courses.all():
            total += course.price

        return total

    def __str__(self):

        course_title = ""

        for course in self.courses.all():
            course_title += course.name
            course_title += ", "

        return 'course=' + course_title + "Student: " + self.Student.first_name + " " + self.Student.last_name
