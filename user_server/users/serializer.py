from rest_framework import serializers
from .models import Account, SigninInfo

class AccountSerializer(serializers.Serializer):
	account = serializers.CharField()
	name    = serializers.CharField()
	age     = serializers.IntegerField()
	job     = serializers.CharField()
	address = serializers.CharField()

	def create(self, validated_data):
		account, flag = Account.objects.get_or_create(**validated_data)
		return account

class SigninInfoSerializer(serializers.Serializer):
	account  = AccountSerializer()
	password = serializers.CharField()

	def create(self, validated_data):
		account_data  = validated_data.pop('account')
		account, flag = Account.objects.get_or_create(**account_data)

		signininfo, flag = SigninInfo.objects.get_or_create(account = account, **validated_data)
		return signininfo
