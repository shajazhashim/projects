from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here.


def index(request):
    courses = Course.objects
    return render(request, 'myfolio/index.html', {'courses': courses})

def details(request, course_id):
    course_detail = get_object_or_404(Course, pk=course_id)
    return render(request, 'myfolio/details.html', {'course': course_detail})