from django.urls import path
from .views import JobList, JobDetail, JobCreate

urlpatterns = [
    path('', JobList.as_view(), name="Job"),
    path('job-create/', JobCreate.as_view(), name="job-create"),
    path('job/<int:pk>/', JobDetail.as_view(), name="jobs-detail")
]