from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomerUrl, CustomerFile
from .serializers import CustomerUrlSerializer, CustomerFileSerializer


class Url(APIView):
    def get(self, request, format=None):
        urls = CustomerUrl.objects.all()
        serializer = CustomerUrlSerializer(urls, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerUrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        data = JSONParser().parse(request)
        request_password = data['password']
        request_url = data['url']

        if request_url[-1:] == "/":
            r_url = request_url[:-1]
            p_url = r_url.split('/')
            id = p_url[-1]
        else:
            p_url = request_url.split('/')
            id = p_url[-1]
        try:
            instance = CustomerUrl.objects.get(pk=id)
        except CustomerUrl.DoesNotExist:
            return HttpResponse(status=404)

        serializer = CustomerUrlSerializer(instance)
        if request_password == instance.password:
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class File(APIView):
    def get(self, request, format=None):
        file = CustomerFile.objects.all()
        serializer = CustomerFileSerializer(file, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        data = JSONParser().parse(request)
        request_password = data['password']
        request_url = data['url']

        if request_url[-1:] == "/":
            r_url = request_url[:-1]
            p_url = r_url.split('/')
            id = p_url[-1]
        else:
            p_url = request_url.split('/')
            id = p_url[-1]
        try:
            instance = CustomerUrl.objects.get(pk=id)
        except CustomerUrl.DoesNotExist:
            return HttpResponse(status=404)

        serializer = CustomerUrlSerializer(instance)
        if request_password == instance.password:
            return Response(serializer.data)
        return Response(serializer.errors, status=400)




