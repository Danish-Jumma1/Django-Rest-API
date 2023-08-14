from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from task.models import Product
from task.serializer import TodoSerializer
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Product.objects.all()
    serializer_class = TodoSerializer