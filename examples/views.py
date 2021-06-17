from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from examples.models import Example
from examples.serializers import ExampleSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST','DELETE'])
def example_list(request):
    # GET list of examples, POST a new example, DELETE all examples
    if request.method == 'GET':
        examples = Example.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            examples = examples.filter(title__icontains=title)

        examples_serializer = ExampleSerializer(examples, many=True)
        return JsonResponse(examples_serializer.data, safe = False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        example_data = JSONParser().parse(request)
        example_serializer = ExampleSerializer(data=example_data)
        if (example_serializer.is_valid()):
            example_serializer.save()
            return JsonResponse(example_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(example_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Example.objects.all().delete()
        return JsonResponse({'message': '{} Examples were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def example_detail(request, pk):
    #find example by pk (id)
    try:
        example = Example.objects.get(pk=pk)
    except Example.DoesNotExist:
        return JsonResponse({'message': 'That example does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET / PUT / DELETE example
    if request.method == 'GET':
        example_serializer = ExampleSerializer(example)
        return JsonResponse(example_serializer.data)
    elif request.method == 'PUT':
        example_data = JSONParser().parse(request)
        example_serializer = ExampleSerializer(example, data=example_data)
        if example_serializer.is_valid():
            example_serializer.save()
            return JsonResponse(example_serializer.data)
        return JsonResponse(example_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        example.delete()
        return JsonResponse({'message': 'Example was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def example_list_published(request):
    # GET all published examples
    examples = Example.objects.filter(published=True)

    if request.method == 'GET':
        examples_serializer = ExampleSerializer(examples, many=True)
        return JsonResponse(examples_serializer.data, safe=False)
