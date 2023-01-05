from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from .models import Job


class JobList(LoginRequiredMixin, ListView):
    model = Job
    context_object_name = 'job'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = context['job'].filter(user=self.request.user)
        context['count'] = context['job'].filter(done=False).count()
        return context


class JobDetail(LoginRequiredMixin, DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'todo/job_detail.html'
    

class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['header', 'info', 'done']
    success_url = reverse_lazy('job')
    
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super(JobCreate, self).form_valid(form)


class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    fields = '__all__'
    success_url = reverse_lazy('job')
    

class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job
    context_object_name = 'job'
    success_url = reverse_lazy('job')
    

class Login(LoginView):
    template_name = 'todo/login.html'
    fields = "__all__"
    redirect_authenticated_user = False
    
    def get_success_url(self):
        return reverse_lazy('job')
