from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TodoSerializers
from .models import Todo

# Todo List CRUD
@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializers(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def todoRead(request):
    data_list = Todo.objects.all()
    serializer = TodoSerializers(data_list, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def todoUpdate(request, pk):
    data_list = Todo.objects.get(id=pk)
    serializer = TodoSerializers(instance=data_list, data=request.data)
    print(serializer)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request, pk):
    data_list = Todo.objects.get(id=pk)
    data_list.delete()
    
    return Response("Delete "+data_list.name + "has success!")