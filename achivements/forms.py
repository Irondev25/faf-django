from django import forms
from django.core.exceptions import ValidationError
from django.conf import settings

from .models import Award,Journal,Conference,Workshop

class AwardForm(forms.ModelForm):
    award_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)

    def __init__(self,*args,**kwargs):
        self.user = kwargs.pop('user')
        super(AwardForm,self).__init__(*args,**kwargs)

    # def clean_fid(self):
    #     fid = self.cleaned_data['fid']
    #     if self.user != fid:
    #         raise ValidationError("Can't create award for other teacher")
    
    class Meta:
        model = Award
        fields = '__all__'

class JournalForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(JournalForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Journal
        fields = '__all__'

class ConferenceForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ConferenceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Conference
        fields = '__all__'


class WorkshopForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(WorkshopForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Workshop
        fields = '__all__'
    
