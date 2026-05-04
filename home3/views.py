from rest_framework.viewsets import ModelViewSet
from .models import Author,Book
from .serializers import AuthSerializer,BookSerializer

class AuthorViewSet(ModelViewSet):
    queryset= Author.objects.all()
    serializer_class = AuthSerializer
class BookViewSet(ModelViewSet):
    queryset= Book.objects.all()
    serializer_class = BookSerializer
    


