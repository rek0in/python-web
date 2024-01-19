import requests
from django.shortcuts import render

def user_list(request):
	response = requests.get('https://randomuser.me/api/?results=10')
	data = response.json().get('results',[])

	context = {'user_list': data}
	return render(request, 'app/user_list.html', context)
