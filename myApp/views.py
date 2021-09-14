from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(response):
    return HttpResponse('HELLO ERBOLBEK!!!!!!!!!!!!!!!!'.title());

def test(request):
    return render(request, 'test/test.html')

def a4(request):
    return render(request, 'test/a4.html')

def a1(request):
    return render(request,'test/a1.html')

def a2(request):
    return render(request,'test/a2.html')

def a3(request):
    return render(request,'test/a3.html')