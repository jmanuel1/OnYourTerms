from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .parser import parse_script
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
	print(request.method)
	if request.method == "POST":
		print(request.body)
	
	context = parse_script.sample_info()
	
	return JsonResponse(context); 