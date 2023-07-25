from django.shortcuts import render

# Create your views here.
def first_1(request):
    return render(request,'first.html')
def second_1(request):
    return render(request,'second.html')