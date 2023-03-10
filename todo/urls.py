from django.urls import path
from .views import JobList, JobDetail, JobCreate, JobUpdate, JobDelete, Login
from .views import SignUp
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', JobList.as_view(), name="jobs"),
    path('job-create/', JobCreate.as_view(), name="job-create"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('job/<int:pk>/', JobDetail.as_view(), name="job-detail"),
    path('job-update/<int:pk>/', JobUpdate.as_view(), name="job-update"),
    path('job-delete/<int:pk>/', JobDelete.as_view(), name="job-delete")
]
