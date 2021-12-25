from rest_framework import serializers
from .models import Account, SigninInfo

# 계정 정보 시리얼라이저 - password 제외 정보들로 구성
class AccountSerializer(serializers.Serializer):
	account = serializers.CharField()
	name    = serializers.CharField()
	age     = serializers.IntegerField()
	job     = serializers.CharField()
	address = serializers.CharField()

	def create(self, validated_data):
		account, flag = Account.objects.get_or_create(**validated_data)
		return account

# 로그인 정보 시리얼라이저 - 사용자 정보 및 password 데이터 동시에 처리
class SigninInfoSerializer(serializers.Serializer):
	account  = AccountSerializer()
	password = serializers.CharField()

	def create(self, validated_data):
		account_data  = validated_data.pop('account')
		account, flag = Account.objects.get_or_create(**account_data)

		signininfo, flag = SigninInfo.objects.get_or_create(account = account, **validated_data)
		return signininfo
