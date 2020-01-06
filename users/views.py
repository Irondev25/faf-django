from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Teacher, Department
from .forms import TeacherChangeForm,TeacherCreationForm

# Create your views here.

def welcome_faculty(request):
    return render(request,'users/teacher_home.html')

@login_required(login_url=reverse_lazy('login'))
def teacher_profile(request,pk):
    return render(request,'users/teacher_profile.html')

class TeacherCreate(generic.CreateView):
    model = Teacher
    form_class = TeacherCreationForm
    success_url = reverse_lazy('login')


class TeacherUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Teacher
    form_class = TeacherChangeForm
    success_url = reverse_lazy('teacher-home')
    login_url = reverse_lazy('login')

@login_required(login_url=reverse_lazy('login'))
def change_password(request):
    if(request.method=='POST'):
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'You password changed successfully')
            return redirect('teacher-home')
        else:
            messages.error(request,"Please correct the error")
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'registration/changed_password.html',{'form':form})


#change hod
