
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# from .bot import agent

def home_view(request):
	return render(request, 'index.html')