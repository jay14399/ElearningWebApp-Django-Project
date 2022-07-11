from django.urls import path

from myapp import views
app_name = 'myapp'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path(r'<int:id>', views.details, name='detail'),
    path(r'courses/', views.courses, name='courses'),
    path(r'place_order/', views.place_order, name='place_order'),
    path(r'courses/<int:cour_id>/', views.course_detail, name='course_detail')
]
