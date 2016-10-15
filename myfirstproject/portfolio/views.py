from django.shortcuts import render

# needed for longhand HttpResponse
from django.http import HttpResponse
from django.template import loader


def index(request):
    # return HttpResponse("<title>le_lel</title><p>here is my portfolio</p>")
    return render(request, 'portfolio/index.html')
