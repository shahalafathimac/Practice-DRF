from django.urls import path
from .views import StudentAPIview

urlpatterns = [
    path('students/',StudentAPIview.as_view()),
]
