from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from .models import Author
from .serializers import AuthorSerializer


# LIST + CREATE
class AuthorListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# RETRIEVE + UPDATE + DELETE
class AuthorDetailView(GenericAPIView,
                       RetrieveModelMixin,
                       UpdateModelMixin,
                       DestroyModelMixin):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
