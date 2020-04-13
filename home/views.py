from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home_view(request):
    return render(request, "index.html", {})

def quote_view(request):
    return render(request, "quote.html", {})

