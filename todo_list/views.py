from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaksSerializer

# Create your views here.
@api_view(['GET'])
def api_overview(request):
    response = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/'
    }
    return Response(response)


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaksSerializer(tasks, many=True)
    return Response(serializer.data)
