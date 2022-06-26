
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.http import HttpResponse




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('myapp/', permanent=True)),
    path(r'myapp/', include('myapp.urls')),

]
