from django.shortcuts import redirect,render
from users.forms import DepartmentChoice
from users.models import Teacher,Department
from django.http import JsonResponse

def index(request):
    teacher = Teacher.objects.all()
    if request.method == 'GET':
        department = request.GET.get('department',None)
        if department is not None:
            teacher = Teacher.objects.filter(department__department_id=department)
        form = DepartmentChoice
    context = {
        'form': form,
        'teacher': teacher
    }
    return render(request,"index.html",context=context)

def achivement_index(request,pk):
    context = {}
    teacher_id = pk
    if teacher_id is not None:
        teacher = Teacher.objects.get(id=teacher_id)
        context.update({'teacher':teacher})
    else:
        return redirect('index')
    return render(request,"achivement_index.html",context=context)