from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Products
from api.serializers import ProductSerializer

# Create your views here.
class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        if "category" in request.query_params:
            cat=request.query_params.get("category")
            qs=qs.filter(category=cat)
        if "price_gt" in request.query_params:
            pr=request.query_params.get("price_gt")
            qs=qs.filter(price__gt=pr)
        if "price_lt" in request.query_params:
            price=request.query_params.get("price_lt")
            qs=qs.filter(price__lt=price)
        if "limit" in request.query_params:
            lm=request.query_params.get("limit")
            qs=qs[:int(lm)]
        sz=ProductSerializer(qs,many=True)
        return Response(data=sz.data)
    def post(self,request,*args,**kwargs):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ProductsDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.get(id=id)
        serializer=ProductSerializer(qs,many=False)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        obj=Products.objects.get(id=id)
        serializer=ProductSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id = kwargs.get("id")
        Products.objects.get(id=id).delete()
        return Response(data="deleted")

class CategoryViews(APIView):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all().values_list("category",flat=True).distinct()
        return Response(data=qs)

