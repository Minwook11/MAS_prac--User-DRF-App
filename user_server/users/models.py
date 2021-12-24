from django.db import models

class Account(models.Model):
	account    = models.CharField(max_length = 64, unique = True)
	name       = models.CharField(max_length = 50)
	age        = models.IntegerField()
	job        = models.CharField(max_length = 128)
	address    = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)

class SigninInfo(models.Model):
	account    = models.ForeignKey(Account, on_delete = models.CASCADE)
	password   = models.CharField(max_length = 128)
	is_usable  = models.BooleanField(default = True)
	created_at = models.DateTimeField(auto_now_add = True)
