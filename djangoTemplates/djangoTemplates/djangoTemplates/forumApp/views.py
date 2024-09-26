from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        "current_time": datetime.now(),
        'ids': ['231', '432'],
        'some_text': '',
        "users": [
            'petar', 'stoyko', 'boyan', 'petkan'
        ]
    }

    return render(request, "base.html", context)

def dashboard(request):
    context = {
    "posts": [
        {
            "title": "How to create django project?",
            "author": "Diyan Kalaydzhiev",
            "content": "I really don't know how to create a project",
            "created_at": datetime.now},
        {
            "title": "How toÏcreate django project?",
            "author": "",
            "content": "I really don't know how to create a project",
            "created_at": datetime.now(),
        },
        {
            "title": "How to create django project?",
            "author": "Diyan Kalaydzhiev",
            "content": "",
            "created_at": datetime.now()}

    ]}

    return render(request, 'dashboard.html', context)



