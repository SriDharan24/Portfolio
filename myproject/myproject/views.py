from django.shortcuts import render
#from django.http import HttpResponse

def homepage(request):
    #return HttpResponse("hi welcome")
    return render(request, 'homepage.html')

def about(request):
    #return HttpResponse("about page")
    return render(request, 'about.html')