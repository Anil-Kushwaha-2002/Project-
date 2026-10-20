from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DataRecord
from .serializers import DataRecordSerializer

from django.shortcuts import render

def home(request):
    return render(request, "dashboard/home.html")  # Updated path

class DataRecordList(APIView):
    def get(self, request):
        data = DataRecord.objects.all()
        serializer = DataRecordSerializer(data, many=True)
        return Response(serializer.data)
