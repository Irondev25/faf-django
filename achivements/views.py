from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

from .models import Award, Journal, Conference, Workshop
from .forms import AwardForm, ConferenceForm, JournalForm, WorkshopForm
from users.models import Teacher


LOGIN_URL = reverse_lazy('login')


class AwardDetailView(DetailView):
    model = Award
    pk_url_kwarg = 'pid'


class AwardCreateView(LoginRequiredMixin, CreateView):
    model = Award
    form_class = AwardForm
    login_url = LOGIN_URL
    success_url = reverse_lazy('teacher-home')

    # def get(self,request,*args,**kwargs):
    #     context = {'form':AwardForm(initial={'fid':request.user.id})}
    #     return render(request,'achivements/award_form.html',context=context)
    def get_initial(self, *args, **kwargs):
        initial = super(AwardCreateView, self).get_initial(**kwargs)
        initial['fid'] = self.request.user.id
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(AwardCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Award Successfully Created")
        return super().form_valid(form)


class AwardUpdateView(LoginRequiredMixin, UpdateView):
    model = Award
    form_class = AwardForm
    #fields = ('award_title','award_date','award_details','certificate')
    login_url = LOGIN_URL
    pk_url_kwarg = 'pid'
    template_name = 'achivements/award_update_form.html'
    success_url = reverse_lazy('teacher-home')

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(AwardUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
            self.object = form.save()
            messages.success(self.request, "Award Successfully Updated")
            return super().form_valid(form)


class AwardDeleteView(LoginRequiredMixin, DeleteView):
    model = Award
    pk_url_kwarg = 'pid'
    success_url = reverse_lazy('teacher-home')
    login_url = LOGIN_URL

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(request, "Award Successfully deleted")
        return HttpResponseRedirect(success_url)


class ConferenceDetailView(DetailView):
    model = Conference
    pk_url_kwarg = 'cid'


class ConferenceCreateView(LoginRequiredMixin, CreateView):
    model = Conference
    form_class = ConferenceForm
    login_url = LOGIN_URL
    success_url = reverse_lazy('teacher-home')

    def get_initial(self, *args, **kwargs):
        initial = super(ConferenceCreateView, self).get_initial(**kwargs)
        initial['fid'] = self.request.user.id
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(ConferenceCreateView,
                       self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Conference Successfully Created")
        return super().form_valid(form)


class ConferenceUpdateView(LoginRequiredMixin, UpdateView):
    model = Conference
    form_class = ConferenceForm
    login_url = LOGIN_URL
    pk_url_kwarg = 'cid'
    template_name = 'achivements/conference_update_form.html'
    success_url = reverse_lazy('teacher-home')

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(ConferenceUpdateView,
                       self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Conference Successfully Updated")
        return super().form_valid(form)


class ConferenceDeleteView(LoginRequiredMixin, DeleteView):
    model = Conference
    pk_url_kwarg = 'cid'
    success_url = reverse_lazy('teacher-home')
    login_url = LOGIN_URL

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(request, "Conference Successfully deleted")
        return HttpResponseRedirect(success_url)



class JournalDetailView(DetailView):
    model = Journal
    pk_url_kwarg = 'pid'


class JournalCreateView(LoginRequiredMixin, CreateView):
    model = Journal
    form_class = JournalForm
    login_url = LOGIN_URL
    success_url = reverse_lazy('teacher-home')

    def get_initial(self, *args, **kwargs):
        initial = super(JournalCreateView, self).get_initial(**kwargs)
        initial['fid'] = self.request.user.id
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(JournalCreateView, self).get_form_kwargs(
            *args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Journal Successfully Created")
        return super().form_valid(form)


class JournalUpdateView(LoginRequiredMixin, UpdateView):
    model = Journal
    pk_url_kwarg = 'pid'
    success_url = reverse_lazy('teacher-home')
    template_name = 'achivements/journal_update_form.html'
    form_class = JournalForm

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(JournalUpdateView, self).get_form_kwargs(
            *args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Journal Successfully Updated")
        return super().form_valid(form)


class JournalDeleteView(LoginRequiredMixin, DeleteView):
    model = Journal
    pk_url_kwarg = 'pid'
    success_url = reverse_lazy('teacher-home')
    login_url = LOGIN_URL

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(request, "Journal Successfully deleted")
        return HttpResponseRedirect(success_url)


class WorkshopDetailView(DetailView):
    model = Workshop
    pk_url_kwarg = 'pid'


class WorkshopCreateView(LoginRequiredMixin, CreateView):
    model = Workshop
    form_class = WorkshopForm
    login_url = LOGIN_URL
    success_url = reverse_lazy('teacher-home')

    def get_initial(self, *args, **kwargs):
        initial = super(WorkshopCreateView, self).get_initial(**kwargs)
        initial['fid'] = self.request.user.id
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(WorkshopCreateView, self).get_form_kwargs(
            *args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Workshop Successfully Created")
        return super().form_valid(form)


class WorkshopUpdateView(LoginRequiredMixin, UpdateView):
    model = Workshop
    pk_url_kwarg = 'pid'
    success_url = reverse_lazy('teacher-home')
    login_url = LOGIN_URL
    template_name = 'achivements/workshop_update_form.html'
    form_class = WorkshopForm

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(WorkshopUpdateView, self).get_form_kwargs(
            *args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
            self.object = form.save()
            messages.success(self.request, "Workshop Successfully Updated")
            return super().form_valid(form)


class WorkshopDeleteView(LoginRequiredMixin, DeleteView):
    model = Workshop
    pk_url_kwarg = 'pid'
    success_url = reverse_lazy('teacher-home')
    login_url = LOGIN_URL

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(request, "Workshop Successfully deleted")
        return HttpResponseRedirect(success_url)




#filter
def filter_awards(request, pk, year):
    awards = Award.objects.filter(
        award_date__year=year, fid__id=pk)
    context = {
        'awards': awards,
        'year': year,
        'faculty': Teacher.objects.get(id=pk)
    }
    return render(request, 'achivements/award_year.html', context=context)


def filter_conferences(request, pk, year):
    conference = Conference.objects.filter(
        date__year=year, fid__id=pk)
    context = {
        'conferences': conference,
        'year': year,
        'faculty': Teacher.objects.get(id=pk)
    }
    return render(request, 'achivements/conference_year.html', context=context)


def filter_journals(request, pk, year):
    journal = Journal.objects.filter(
        date__year=year, fid__id=pk)
    context = {
        'journals': journal,
        'year': year,
        'faculty': Teacher.objects.get(id=pk)
    }
    return render(request, 'achivements/journal_year.html', context=context)


def filter_workshops(request, pk, year):
    print(pk)
    workshop = Workshop.objects.filter(
        date__year=year, fid__id=pk)
    context = {
        'workshops': workshop,
        'year': year,
        'faculty': Teacher.objects.get(id=pk)
    }
    return render(request, 'achivements/workshop_year.html', context=context)

