from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import *
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
import sys
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import HttpResponse,JsonResponse



# Create your views here.
def index(request):
    if request.method=="POST":
        print (request.POST.get('search'))
    return render(request,'index.html',{})
def test(request):
    return render(request,'test.html',{})



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def post(self,request):
    #     print (request)
    #     context={}
    #
    #
    #     return Response(context,status=status.HTTP_200_OK)

    # @csrf_exempt
    # def get(self,request):
    #     s=ProductSerializer
    #     print(request)
    #     return Response(s.data)

@csrf_exempt
@api_view(['GET'])
def BrandViewSet(request):
    print (request.method)
    if request.method=="GET":

        brands=Brands.objects.all()
        serial=BrandsSerializer(brands,{'request':request},many=True)
        print (serial.data)
        return Response(serial)
# @api_view(['POST'])
# def postTst(request):
#     # print (request.POST['name'])
#     context={}
#     # context['email']=request.POST.get('email')
#     # context['password'] = request.POST.get('password')
#     # print(request.data)
#     if request.method=="POST":
#
#         context['price']=request.POST.get('price',0)
#         context['serial_number']=request.POST.get('serial_number',0)
#         context['brand_name']=request.POST.get('brand_name')
#         context['store_name']=request.POST.get('store_name')
#         print(context)
#         return HttpResponse('sucess')
#         # return Response(context,status=status.HTTP_200_OK)
#     return Response(context,status=status.HTTP_200_OK)

class postTst(APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)


    def post(self, request):

        user = request.data
        print(request.data)
        print(user)
        try:

            obj=Users(email=request.data['email'],password=request.data['password'])

            # serializer=userSerializer(email=request.data['email'],password=request.data['password'])

            # serializer.save()
        except:
            print sys.exc_info()
            # serializer.is_valid(raise_exception=True)

        return Response({'foo':'bar'}, status=status.HTTP_201_CREATED)


def get_json_list(query_set):
    list_objects = []
    for obj in query_set:
        dict_obj = {}
        for field in obj._meta.get_fields():
            try:
                if field.many_to_many:
                    dict_obj[field.name] = get_json_list(getattr(obj, field.name).all())
                    continue
                dict_obj[field.name] = getattr(obj, field.name)
            except AttributeError:
                continue
        list_objects.append(dict_obj)
    return list_objects



