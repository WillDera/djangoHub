from django.shortcuts import render
import requests
# # import the logging library
# import logging

# # Get an instance of a logger
# logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    data = {}
    if 'username' in request.GET:
        username = request.GET['username']
        # url = 'https://api.github.com/users/%s/repos' % username
        response = requests.get(
            'https://api.github.com/users/%s/repos' % username)
        search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
        data = response.json()
        data[0] = search_was_successful
        # data['rate'] = {
        #     'limit': response.headers['X-RateLimit-Limit'],
        #     'remaining': response.headers['X-RateLimit-Remaining'],
        # }

    return render(request, 'gitReq/index.html', {'data': data})
