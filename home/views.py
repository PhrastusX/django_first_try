from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
import requests
from django.contrib.auth.models import User


def home(request):
	data = {}
	tnow = datetime.now()
	data['time'] = tnow
	

	return render(request, 'home.html', data)

