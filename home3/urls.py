from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet,BookViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='authors')
router.register('book', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]