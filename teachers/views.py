from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher
from .serializers import TeacherSerializer


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
class TeacherDetailView(APIView):
    def get(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)