from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import AccountSerializer, PasswordSerializer, WriteSigninInformationSerializer

@api_view(['POST'])
def SignUp(request):
	if request.method == 'POST':
		serializer_class = WriteSigninInformationSerializer(data = request.data)

		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status = status.HTTP_200_OK)
		else:
			return Response(status = status.HTTP_400_BAD_REQUEST)
