from django.urls import path
from .views import JobList, JobDetail

urlpatterns = [
    path('', JobList.as_view(), name="Job"),
    path('job/<int:pk>/', JobDetail.as_view(), name="jobs-detail")
]