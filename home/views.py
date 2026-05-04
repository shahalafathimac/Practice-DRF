from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import LoginSerializer,RegisterSerializer


class RegisterAPIView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "registered successfully"
            },status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            return Response({
                "login successfully"
            },status=status.HTTP_200_OK)
    
        return Response(serializer.errors, status=status.HTTP_400__BAD_REQUEST)

