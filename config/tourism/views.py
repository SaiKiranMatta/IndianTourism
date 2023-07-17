from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tourism/index.xhtml')

def popular(request):
    return render(request, 'tourism/Popular.xhtml')

def about(request):
    return render(request, 'tourism/AboutUs.xhtml')

def contact(request):
    return render(request, 'tourism/contactus.html')

def gallery(request):
    return render(request, 'tourism/Gallery.xhtml')

def bystate(request):
    return render(request, 'tourism/bystate.xhtml')

def bytype(request):
    return render(request, 'tourism/bytype.xhtml')

