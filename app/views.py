from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def String_response4(request):
    return HttpResponse('<h1><marquee>Love Laughter Happily Ever After</h1></marquee>')