from django.db import models,connection
from django.contrib.auth.models import AbstractUser
import time

from .queries import get_award_year, get_conference_year, get_journal_year, get_workshop_year

# Create your models here.


def file_pic(instance, filename):
    return 'user_{0}/pic/{2}_{1}'.format(instance.id, filename, time.time())


class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=100)
    hodid = models.ForeignKey('Teacher',on_delete=models.SET_NULL,null=True,related_name='hod')

    def __str__(self):
        return self.department_name


class Teacher(AbstractUser):
    profile_pic = models.ImageField(verbose_name="Profile Picture",blank=True,null=True,upload_to=file_pic,default='default.png')
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    dob = models.DateField(verbose_name='Date Of Birth', null=True)
    doj = models.DateField(verbose_name='Date Of Join', null=True)
    mobile_num = models.CharField(verbose_name='Mobile Number',max_length=10,null=True,blank=True)

    SEX_CHOICE = (
        ('m','Male'),
        ('f','Female'),
        ('t','Transgender'),
        ('o','Others')
    )
    sex = models.CharField(max_length=1,choices=SEX_CHOICE,default='m')
    department = models.ForeignKey('Department',on_delete=models.SET_NULL,null=True)

    @property
    def is_hod(self):
        if self.department.hodid is not None:
            if self.department.hodid.id == self.id:
                return True
        return False
    
    @property
    def award_years(self):
        return get_award_year(self)
    
    @property
    def conference_years(self):
        return get_conference_year(self)
    
    @property
    def journal_years(self):
        return get_journal_year(self)
    
    @property
    def workshop_years(self):
        return get_workshop_year(self)
    
    
    def __str__(self):
        return self.first_name+' '+self.last_name
    
    def sex_verbose(self):
        return dict(Teacher.SEX_CHOICE)[self.sex]

    
