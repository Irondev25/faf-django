from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.conf import settings

from .models import Teacher,Department
from django import forms

import datetime


class TeacherCreationForm(UserCreationForm):
    dob = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, required=False)
    doj = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,required=False)

    # def clean_dob(self):
    #     data = self.cleaned_data['dob']
    #     if(data > datetime.date.today()):
    #         raise ValidationError("Invalid Date of Birth(date in future)")
    
    # def clean_doj(self):
    #     doj_data = self.cleaned_data['doj']
    #     if(doj_data > datetime.date.today()):
    #         raise ValidationError("Invalid Date of Join(date in future)")


    class Meta(UserCreationForm):
        model = Teacher
        fields = ('username', 'email', 'mobile_num', 'first_name',
                  'middle_name', 'last_name', 'dob', 'doj', 'sex', 'department','profile_pic')



class TeacherChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = Teacher
        fields = ('username', 'email', 'mobile_num', 'first_name',
                  'middle_name', 'last_name', 'dob', 'doj', 'sex', 'department','profile_pic')


class DepartmentChoice(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all())