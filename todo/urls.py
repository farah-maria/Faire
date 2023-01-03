from django.urls import path
from .views import JobList, JobDetail, JobCreate, JobUpdate, JobDelete, Login


urlpatterns = [
    path('', JobList.as_view(), name="job"),
    path('job-create/', JobCreate.as_view(), name="job-create"),
    path('login/', Login.as_view(), name="login"),
    path('job/<int:pk>/', JobDetail.as_view(), name="job-detail"),
    path('job-update/<int:pk>/', JobUpdate.as_view(), name="job-update"),
    path('job-delete/<int:pk>/', JobDelete.as_view(), name="job-delete")
]