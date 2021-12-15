from django.db import models

class Account(models.Model):
	account = models.CharField(max_length = 64, unique = True)
	name = models.CharField(max_length = 50)
	age = models.IntegerField()
	job = models.CharField(max_length = 128)
	address = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)

class Password(models.Model):
	password = models.CharField(max_length = 128)

class DeliveryAddress(models.Model):
	address = models.TextField()

class SigninInformation(models.Model):
	user = models.ForeignKey(Account, on_delete = models.CASCADE)
	password = models.ForeignKey(Password, on_delete = models.CASCADE)
	is_usable = models.BooleanField(default = True)
	created_at = models.DateTimeField(auto_now_add = True)

class AddressBook(models.Model):
	name = models.CharField(max_length = 64)
	user = models.ForeignKey(Account, on_delete = models.CASCADE)
	deliveryaddress = models.ForeignKey(DeliveryAddress, on_delete = models.CASCADE)
