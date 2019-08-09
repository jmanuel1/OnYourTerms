from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .parser import parse_script
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def fetch_info(request):
	if request.method == "POST":
		split_list = (request.body).decode("utf-8").split("\n")
		url = split_list[len(split_list) - 3].replace("\n", "")
		

	context = parse_script.sample_info()
	
	return JsonResponse(context)