from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import File,Product,Category
from .serializers import( FileSerializer,CategorySerializer,ProductSerializer)



class ProductListView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True,context={"request":request})
        return Response(serializer.data)

    # post dorost kar nakard
    # def post(self,request):
    #     serializer=ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            product=Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        return product

    def get(self,request,pk):
        product=self.get_object(pk)
        serializer=ProductSerializer(product,context={"request":request})
        return Response(serializer.data)

    # def delete(self, request, pk):
    #     product = self.get_object(pk)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


    # put dorost kar nakard
    # def put(self,request,pk):
    #     product=self.get_object(pk)
    #     serializer=ProductSerializer(product,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
class CategoryListView(APIView):
    def get(self,request,product_id):
        categories=Category.objects.filter(id=product_id)
        serializer=CategorySerializer(categories,many=True,context={"request":request})
        return Response(serializer.data)
class CategoryDetailView(APIView):

    def get_object(self, product_id,pk):
        try:
            category = Category.objects.get(pk=pk,id=product_id)
        except Category.DoesNotExist:
            raise Http404
        return category

    def get(self, request,product_id,pk):
        category = self.get_object(pk,product_id)
        serializer = CategorySerializer(category, context={"request": request})
        return Response(serializer.data)
class FileListView(APIView):
    def get(self,request,product_id):
        files=File.objects.filter(product_id=product_id)
        serializer=FileSerializer(files,many=True,context={"request":request})
        return Response(serializer.data)
class FileDetailView(APIView):
    def get_object(self,product_id,pk):
        try:
            file = File.objects.get(pk=pk,product_id=product_id)
        except File.DoesNotExist:
            raise Http404
        return file

    def get(self,request,product_id,pk):
        file=self.get_object(product_id,pk)
        serializer=FileSerializer(file,context={"request":request})
        return Response(serializer.data)


