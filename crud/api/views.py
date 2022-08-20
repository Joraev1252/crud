from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from crud.models import Account
from crud.api.serializers import AccountSerializers


@api_view(['POST', ])
def send_data_view(request):

    if request.method == 'POST':
        serializer = AccountSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Data successfully sent!!"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def update_data_view(request, pk):
    try:
        data = Account.objects.get(id=pk)
    except Account.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AccountSerializers(data, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Data successfully updated."
            return Response(data=data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', ])
def data_view(request):
    if request.method == 'GET':
        data = Account.objects.all()
        serializer = AccountSerializers(data, many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
def data_delete(request, pk):
    blog = Account.objects.get(id=pk)
    blog.delete()
    return Response('Data successfully deleted!')






