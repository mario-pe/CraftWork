from rest_framework import generics
from rest_framework import serializers
from .models import CustomerUrl, CustomerFile
from .serializers import CustomerFileSerializer, CustomerUrlSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


@csrf_exempt
def url_add(request):           #autoryzacja

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerUrlSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'GET':
        snippets = CustomerUrl.objects.all()
        serializer = CustomerUrlSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_url(request, pk):
# def url_get_by_id(request, password, id):

    # r_url = request_url[:-1]
    # print(r_url)
    # pk =

    try:
        url = CustomerUrl.objects.get(pk=pk)
    except CustomerUrl.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CustomerUrlSerializer(url)
        # if url.password == password:
        return JsonResponse(serializer.data)
        # return JsonResponse(serializer.errors, status=400)



