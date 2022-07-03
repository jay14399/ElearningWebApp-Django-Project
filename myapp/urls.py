from argparse import Namespace
from django.urls import path
from myapp import views
app_name = 'myapp'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path(r'<int:id>', views.details, name='detail'),
    path(r'courses/', views.courses, name='courses'),
]
