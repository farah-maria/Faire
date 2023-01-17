from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Job


class JobList(LoginRequiredMixin, ListView):
    model = Job
    context_object_name = 'jobs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = context['jobs'].filter(user=self.request.user)
        context['count'] = context['jobs'].filter(done=False).count()
        return context


class JobDetail(LoginRequiredMixin, DetailView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'todo/job_detail.html'


class JobCreate(LoginRequiredMixin, CreateView):

    model = Job
    fields = ['header', 'info', 'done']
    success_url = reverse_lazy('jobs')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobCreate, self).form_valid(form)


class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['header', 'info', 'done']
    success_url = reverse_lazy('jobs')


class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job
    context_object_name = 'jobs'
    success_url = reverse_lazy('jobs')


class Login(LoginView):
    template_name = 'todo/login.html'
    fields = "__all__"
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('jobs')


class SignUp(FormView):
    template_name = 'todo/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('jobs')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUp, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return_redirect('jobs')
        return super(SignUp, self).get(*args, **kwargs)
