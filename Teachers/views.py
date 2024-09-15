from .forms import TeacherForm, PupilForm
from .models import Teacher
from django.shortcuts import render, redirect

def teacher_register(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():



            for key, value in form.cleaned_data.items():
                print(f'{key}: {value}')
            form.save()

            return redirect('success')
    else:
        form = TeacherForm()
    return render(request, 'teacher_register.html', {'form': form})

def success(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_success.html', {'teachers': teachers})

def index(request):
    return render(request, 'index.html')

def update(request, id):
    teacher = Teacher.objects.get(id=id)
    for key, value in teacher.__dict__.items():
        print(f'{key}: {value}')
    form = TeacherForm(request.POST or None, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect('success')
    return render(request, 'teacher_update.html', {'form': form, 'teacher': teacher})

def delete(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return redirect('success')

def pupil_register(request):
    if request.method == 'POST':
        form = PupilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PupilForm()
    return render(request, 'teacher_register.html', {'form': form})
