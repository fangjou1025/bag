from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Create your views here.
def boy(request):
    return render(request, 'boy/boy.html')
