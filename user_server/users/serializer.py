from rest_framework import serializers
from .models import Account, Password, DeliveryAddress, SigninInformation, AddressBook

class AccountSerializer(serializers.Serializer):
	account = serializers.CharField()
	name = serializers.CharField()
	age = serializers.IntegerField()
	job = serializers.CharField()
	address = serializers.CharField()

	def create(self, validated_data):
		account, flag = Account.objects.get_or_create(**validated_data)
		return account

class PasswordSerializer(serializers.Serializer):
	password = serializers.CharField()

	def create(self, validated_data):
		password, flag = Password.objects.get_or_create(**validated_data)
		return password

class WriteSigninInformationSerializer(serializers.Serializer):
	user = AccountSerializer()
	password = PasswordSerializer()

	def create(self, validated_data):
		user_data = validated_data.pop('user')
		user, flag = Account.objects.get_or_create(**user_data)
		password, flag = Password.objects.get_or_create(password = validated_data['password']['password'])

		signininform, flag = SigninInformation.objects.get_or_create(user = user, password = password)
		return signininform
