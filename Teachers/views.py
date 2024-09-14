from .forms import TeacherForm
from .models import Teacher
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TeacherForm()
    return render(request, 'register.html', {'form': form})

def success(request):
    teachers = Teacher.objects.all()
    
    return render(request, 'success.html', {'teachers': teachers})

def index(request):
    return render(request, 'index.html')