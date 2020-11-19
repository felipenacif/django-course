from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return render(
        request,
        'home/home_page.html',
        {
            'name': 'Felipe',
            'date': datetime.now()
        }
    )