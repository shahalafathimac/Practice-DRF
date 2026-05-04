from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author
from .serializers import AuthorSerializer


class AuthorAPIView(APIView):

    
    def get(self, request, pk=None):
        if pk:
            author = Author.objects.get(id=pk)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)

        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)


    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Author created successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
    def put(self, request, pk):
        author = Author.objects.get(id=pk)
        serializer = AuthorSerializer(author, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated successfully"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
    def delete(self, request, pk):
        author = Author.objects.get(id=pk)
        author.delete()
        return Response({"message": "Deleted successfully"})
