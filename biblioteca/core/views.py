from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .models import Livro
from .serializers import LivroSerializer


@csrf_exempt
def livro_list_create(request):
    if request.method == 'GET':
        livros = Livro.objects.all() # pylint: disable=no-member
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def livro_detail(request, pk):
    livro = Livro.objects.get(pk=pk) # pylint: disable=no-member

    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method =='DELETE':
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
