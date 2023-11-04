from django.shortcuts import render
from students.models import Student
from students.serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

#CRUD-  create, read, update, delete

# Create your views here.
@api_view(['GET','POST'])
@csrf_exempt
def students_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializers = StudentSerializers(students,many=True)
        return Response(serializers.data)

    elif(request.method == 'POST'):
        serializers = StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
   
api_view(['GET','PUT','DELETE'])
@csrf_exempt
def students_details(request,pk):
    print(pk)
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print(student)
        serializers = StudentSerializers(Student)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = StudentSerializers(Student,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)