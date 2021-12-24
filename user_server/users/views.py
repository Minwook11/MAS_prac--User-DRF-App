from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import AccountSerializer,SigninInfoSerializer
from .models import Account

@api_view(['GET'])
def accountDuplicate(request):
	if request.method == 'GET':
		duplicate_check = Account.objects.filter(account = request.data['account'])

		if duplicate_check:
			return Response(
					data   = {"detail" : "The account is alread exists"}, 
					status = status.HTTP_400_BAD_REQUEST)
		else:
			return Response(
					data   = {"detail" : "Available account"}, 
					status = status.HTTP_200_OK)

@api_view(['POST'])
def signUp(request):
	if request.method == 'POST':
		serializer_class = SigninInfoSerializer(data = request.data)

		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status = status.HTTP_200_OK)
		else:
			return Response(status = status.HTTP_400_BAD_REQUEST)
