from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Job


class JobList(ListView):
    model = Job
    context_object_name = 'job'
