# from django.shortcuts import render

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView
# from .models import Task
# from .serializers import TaskSerializer, AssignTaskSerializer

# # API to create a task
# class TaskCreateView(ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# # API to assign users to a task
# class AssignTaskView(UpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = AssignTaskSerializer

# # API to retrieve tasks assigned to a specific user
# class UserTasksView(APIView):
#     def get(self, request, user_id):
#         tasks = Task.objects.filter(assigned_users__id=user_id)
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)



from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer, AssignTaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def perform_create(self, serializer):
        serializer.save()
