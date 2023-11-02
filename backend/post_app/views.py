from django.shortcuts import render
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.generics import CreateAPIView,ListCreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView,ListAPIView
# Create your views here.

class EmployeeAPI(CreateAPIView,ListAPIView):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()

class EmployeeDETAPI(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()    