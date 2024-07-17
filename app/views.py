from django.shortcuts import render, redirect
from app.models import Student
from django.contrib import messages

# Create your views here.
def home(requests):
    return render(requests, 'web/index.html')
def profile(requests, profile):
    return render(requests, 'web/profiles.html',
     {'profile': favour})
def student(requests):
    all_students = Student.objects.all()
    context = {'data': all_students}

    return render(requests, 'web/studentr.html', context)
def newstudent(requestd):
    if requests.method == "POST":
        name = request.POST.get("name")
        reg_number = requests.POST.GET("Registration")
        age = requests.POST.GET("age")
        cgpa = requests.POST.GET("cgpa")
        dj = requests.POST.GET("datejoined")
        if not name or not reg_number or not age or not cgpa or not dj:
            messages.error(requests, "ALL fields are required")
            return redirect(newstudent)
    print("hey")
    return render(requests, 'web/newstudent')
