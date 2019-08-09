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
		
	url = "https://www.jetblue.com/legal/flights-terms"
	context = parse_script.sample_info()
	
	response = JsonResponse(context)
	response['Access-Control-Allow-Origin'] = '*'
	response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
	response["Access-Control-Max-Age"] = "1000"
	response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
	
	return response