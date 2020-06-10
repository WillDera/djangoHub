from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = request.get(url)
        user = response.json()
    return render(request, 'gitReq/index.html', {'user': user})