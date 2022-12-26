from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from .models import DRF_Test
from .serializers import DRF_TestSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
class DRF_TestAPIView(APIView):


    # Для создания
    def post(self, request, format=None):
        data = request.data
        seleriazer = DRF_TestSerializer(data=data)
        if seleriazer.is_valid():
            seleriazer.seve()
            return Response(seleriazer.data, status=status.HTTP_201_CREATED)
        return Response(seleriazer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Для обнавления
    def put(self, request, pk, format=None):
        student_obj = DRF_Test.objects.get(pk=pk)
        serializer = DRF_TestSerializer(data=request.date, instance=student_obj)
        if serializer.is_valid():
            serializer.save()
            return Response('Message : Data Updated Succefuly')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Это для частичного обновления
    def patch(self, request, pk=None, format=None):
        student_obj = DRF_Test.objects.get(pk=pk)
        serializer = DRF_TestSerializer(data=request.date, instance=student_obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('Message : Data Updated Succefuly')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Это для получения сиглнала объекта или всех объектов
    def get(self, request, pk=None, format=None):
        try:
            if pk:
               student_obj = DRF_Test.objects.get(pk=pk)
               serializer = DRF_TestSerializer(student_obj)
            else:
                queryset = DRF_Test.objects.all()
                serializer = DRF_TestSerializer(queryset, many=True)
        except Exception:
            return HttpResponseRedirect('/api/drf_test/')
        return Response(serializer.data)

    # Для удаления
    def delete(self, request, pk=None, format=None):
        DRF_Test.objects.get(pk=pk).delete()
        return Response({"Message": "Data Deleted Successfully!!"})
