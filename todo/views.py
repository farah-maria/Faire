from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
from .models import Job


class JobList(ListView):
    model = Job
    context_object_name = 'job'


class JobDetail(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'todo/job_detail.html'
    

class JobCreate(CreateView):
    model = Job
    fields = '__all__'
    success_url = reverse_lazy('job')


class JobUpdate(UpdateView):
    model = Job
    fields = '__all__'
    success_url = reverse_lazy('job')
    

class JobDelete(DeleteView):
    model = Job
    context_object_name = 'job'
    success_url = reverse_lazy('job')
    

class Login(LoginView):
    template_name = 'todo/login.html'
    fields = "__all__"
    redirect_authenticated_user = False
    
    def get_success_url(self):
        return reverse_lazy('job')