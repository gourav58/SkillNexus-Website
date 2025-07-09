from django.shortcuts import render

def Home(request):
    return render(request, 'home.html')

def Aboutus(request):
    return render(request, 'aboutus.html')

def Services(request):
    return render(request, 'services.html')

def Courses(request):
    return render(request, 'courses.html')

def Blog(request):
    return render(request, 'blog.html')

def Contactus(request):
    return render(request, 'contactus.html')

def BookDemo(request):
    return render(request, 'bookdemo.html')
