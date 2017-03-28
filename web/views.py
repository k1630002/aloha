from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	if request.user.is_authenticated():
		return redirect('profile')
	else:
		return render(request, 'web/index.html')

def signup(request):
	return render(request, 'web/signup.html')

@login_required(login_url='/')
def profile(request):
	return render(request, 'web/profile.html')