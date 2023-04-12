from django.shortcuts import render

# Create your views here.


def homeSite(request):
    return render(request, 'home.html')
