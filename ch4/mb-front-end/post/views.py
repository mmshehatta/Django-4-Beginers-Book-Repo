from django.shortcuts import render
import requests


def post_list(request):
    BASE_URL = "http://localhost:8000"
    HEADERS = {"Content-Type":"Application/json"}

    response = requests.get(BASE_URL , headers=HEADERS)

    posts = response.json()

    return render(request , "index.html" , {"posts":posts["Results"]})



