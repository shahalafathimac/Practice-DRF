from django.urls import path
from .views import AuthorAPIView

urlpatterns = [
    path('authors/', AuthorAPIView.as_view()),
    path('authors/<int:pk>/', AuthorAPIView.as_view()),
]