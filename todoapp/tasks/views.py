from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Tasks
from .serializers import TaskSerializer

@api_view(['GET'])
def get_tasks(request):
    tasks = Tasks.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_task(request, pk):
    task = Tasks.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_task(request, pk):
    task = Tasks.objects.get(id=pk)
    task.delete()
    return Response('Task deleted')
