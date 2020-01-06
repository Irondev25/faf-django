from django.db import models
from django.shortcuts import reverse
from django.conf import settings

import time

from users.models import Teacher

# Create your models here.

def file_award(instance,filename):
    return 'user_{0}/award/{2}_{1}'.format(instance.fid.id,filename,time.time())

def file_conference(instance,filename):
    return 'user_{0}/conference/{2}_{1}'.format(instance.fid.id, filename, time.time())

def file_journal(instance, filename):
    return 'user_{0}/journal/{2}_{1}'.format(instance.fid.id, filename, time.time())

def file_workshop(instance, filename):
    return 'user_{0}/workshop/{2}_{1}'.format(instance.fid.id, filename, time.time())

class Award(models.Model):
    pid = models.AutoField(primary_key=True)
    award_title = models.CharField(help_text="Title Of Award",max_length=200)
    award_date = models.DateField(verbose_name="Awarded On",null=True,blank=True)
    award_details = models.TextField(null=True,blank=False)
    certificate = models.FileField(upload_to=file_award,null=True,blank=True)
    fid = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.award_title
    
    def get_absolute_url(self):
        return reverse('award-detail',args=[self.fid.id,self.pid])
    
    class Meta:
        ordering = ['award_date','award_title']


TYPE_CHOICE = (
    ('N', 'National'),
    ('IN', 'International'),
    ('IEEE-N', 'IEEE-National'),
    ('IEEE-IN', 'IEEE-International')
)

class Conference(models.Model):
    #pid = models.IntegerField(primary_key=True,editable=False)
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="Conference Name")
    title = models.CharField(max_length=200, help_text="Enter Title")
    date = models.DateField(verbose_name="Date of Conference",blank=True,null=True)
    TYPE_CHOICE = (
        ('N','National'),
        ('IN','International'),
        ('IEEE-N','IEEE-National'),
        ('IEEE-IN','IEEE-International')
    )
    certificate = models.FileField(upload_to=file_conference, null=True, blank=True)
    conference_type = models.CharField(choices=TYPE_CHOICE,max_length=20,default='N')
    fid = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('conference-detail', args=[self.fid.id, self.pid])

    def conference_type_verbose(self):
        return dict(TYPE_CHOICE)[self.conference_type]

    class Meta:
        ordering = ['date','name','title']
    
class Journal(models.Model):
    pid = models.AutoField(primary_key=True)
    journal_title = models.CharField(verbose_name="Title of Journal",max_length=200)
    paper_title = models.CharField(verbose_name="Title of Paper", max_length=200)
    date = models.DateField(verbose_name="Journal Presentation Date",blank=True,null=False)
    journal_type = models.CharField(
        max_length=20, choices=TYPE_CHOICE, default='N')
    impact_factor = models.FloatField(blank=True,null=True)
    certificate = models.FileField(upload_to=file_journal, null=True, blank=True)
    fid = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.journal_title
    
    def get_absolute_url(self):
        return reverse('journal-detail', args=[self.fid.id, self.pid])
    
    def journal_type_verbose(self):
        return dict(TYPE_CHOICE)[self.journal_type]
    
    class Meta:
        ordering = ['date','journal_title', 'paper_title']

class Workshop(models.Model):
    pid = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=200,verbose_name="Workshop Title")
    date = models.DateField(verbose_name="Held on",blank=True,null=True)
    workshop_type = models.CharField(
        choices=TYPE_CHOICE, max_length=20, default='N')
    location = models.CharField(verbose_name="Held at(location)",max_length=200)
    certificate = models.FileField(upload_to=file_workshop, null=True, blank=True)
    fid = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.topic
    
    def get_absolute_url(self):
        return reverse('workshop-detail', args=[self.fid.id, self.pid])
    
    def workshop_type_verbose(self):
        return dict(TYPE_CHOICE)[self.workshop_type]
    
    class Meta:
        ordering = ['date', 'topic']
