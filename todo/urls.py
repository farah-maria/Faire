from django.urls import path
from .views import JobList, JobDetail, JobCreate, JobUpdate

urlpatterns = [
    path('', JobList.as_view(), name="job"),
    path('job-create/', JobCreate.as_view(), name="job-create"),
    path('job/<int:pk>/', JobDetail.as_view(), name="jobs-detail"),
    path('job-update/<int:pk>/', JobUpdate.as_view(), name="jobs-update")
]