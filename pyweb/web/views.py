from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
    # return HttpResponse("This  is  homepage")

def Class(request):
    return render(request, 'Class.html')
    # return HttpResponse("This  is  class")

def Know_more(request):
    return render(request, 'Know_more.html')
    #return HttpResponse("This  is  Know_more")

def Contact_us(request):
    return render(request, 'Contact_us.html')
    #return HttpResponse("This  is  Contact_us")

def login_page(request):
    return render(request, 'login_page.html')

def firstpage(request):
    return render(request, 'firstpage.html')