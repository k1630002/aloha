from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import json

def login(request):
	data = json.loads(request.body)
	username = data['username']
	password = data['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		auth_login(request, user)
		return HttpResponse()
	else:
		return HttpResponseForbidden()

def logout(request):
	auth_logout(request)
	return HttpResponse()

def register(request):
	data = json.loads(request.body)
	user = User.objects.create_user(
		data['username'], 
		data['email'], 
		data['password'], 
		first_name=data['first_name'], 
		last_name=data['last_name'])
	return HttpResponse('this is registration');