from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
import json

# Create your views here.

def messages(request):
    return HttpResponse("Hello, world. You're at the messages index.")

def chats(request):
    return HttpResponse("Hello, world. You're at the chat index.")

