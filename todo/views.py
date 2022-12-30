from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Job


class JobList(ListView):
    model = Job
    context_object_name = 'job'


class JobDetail(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'todo/job_detail.html'