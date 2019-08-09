from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .parser import parse_script
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def fetch_info(request):
	url = "https://www.jetblue.com/legal/flights-terms"
	if request.method == "POST":
		split_list = (request.body).decode("utf-8").split("\n")
		#print(split_list[0])
		
		#url = split_list[len(split_list) - 3].replace("\n", "")
		url = split_list[0]
		#print(url[1:len(url) - 1])
		
	context = {
		"data": parse_script.parse_url(url) 
	}
	
	print(context)
	
	response = JsonResponse(context)
	response['Access-Control-Allow-Origin'] = '*'
	response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
	response["Access-Control-Max-Age"] = "1000"
	response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
	
	return response