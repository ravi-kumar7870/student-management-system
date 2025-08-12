# Create your views here.
from django.shortcuts import render 
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Student
from .forms import StudentForm

def home(request):
    return render(request, 'students/home.html')
    

def student_list(request):
    q = request.GET.get('q', '')
    students = Student.objects.all().order_by('-created_at')
    if q:
        students = students.filter(Q(name__icontains=q) | Q(roll_number__icontains=q) | Q(course__icontains=q))
    paginator = Paginator(students, 10)
    page = request.GET.get('page')
    students = paginator.get_page(page)
    return render(request, 'students/student_list.html', {'students': students, 'q': q})

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added.")
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated.")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/add_student.html', {'form': form, 'edit': True})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted.")
        return redirect('student_list')
    return render(request, 'students/confirm_delete.html', {'student': student})

