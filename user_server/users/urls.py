from django.urls import path
from . import views

urlpatterns = [
	path('/duplicate', views.accountDuplicate),
	path('/signup', views.signUp),
]
