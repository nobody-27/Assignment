from django.shortcuts import render
from django.views.generic import View
a="32432"

from rest_framework.views import APIView
from rest_framework.response import Response
from books_app.serializers import Bookserializer,Videoserializer
from books_app.models import Book
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from books_app.utils import (
    generate_video,handle_uploaded_image
)

# Create your views here.


class Home_View(View):
    template_name = "books_app/home.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)



#API 
class Books_Apiview(APIView):
    serializer_class = Bookserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_book_or_404(self,book_id):
        return get_object_or_404(Book,id=book_id)
    
    def get(self,request,pk=None):
        if pk is not None:
            book = get_object_or_404(Book, id=pk)
            return Response({"data": self.serializer_class(book).data}, status=status.HTTP_200_OK)
        
        books = Book.objects.all()
        return Response({"data": self.serializer_class(books, many=True).data}, status=status.HTTP_200_OK)
    
    def post(self,request):
        books_obj = self.serializer_class(data=request.data)
        if books_obj.is_valid():
            books_obj.save()
            return Response({"message": "Book successfully saved!", "data": books_obj.data}, status=status.HTTP_201_CREATED)
        
        return Response({"message": "Failed to save book", "errors": books_obj.errors}, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self,request,pk):
        book = self.get_book_or_404(pk)
        serializer = self.serializer_class(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Book successfully updated", "data": serializer.data}, status=status.HTTP_200_OK)
        
        return Response({"message": "Failed to update book", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        book = self.get_book_or_404(pk)
        serializer = self.serializer_class(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Book partially updated", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"message": "Failed to partially update book", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        book = self.get_book_or_404(pk)
        book.delete()
        
        return Response({"message": "book deleted sucessfully!",}, status=status.HTTP_204_NO_CONTENT)


class GenerateVideoAPIView(APIView):
    serializer_class = Videoserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            uploaded_image = request.FILES.get('images')
            image_path = handle_uploaded_image(uploaded_image)
            video_path = generate_video(image_path)

            return Response({"message": f"Video generated successfully.", "video_path": video_path}, status=status.HTTP_201_CREATED)
        
        return Response({"message": "Invalid data.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)





    

    