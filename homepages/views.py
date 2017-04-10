from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'homepages/index.html')

def graphics(request):
    return render(request,'grafic.html')

def text(request):
    return render(request,'homepages/text.html')

def demografia(request):
    return render(request,'homepages/demografia.html')

def tranzitia(request):
    return render(request,'homepages/tranzitia.html')

def istoric(request):
    return render(request,'homepages/istoric.html')
def donatii(request):
    return render(request, 'homepages/donatii.html')

def dash(request):
    return render(request,'common/base.html')