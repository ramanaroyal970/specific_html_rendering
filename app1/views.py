from django.shortcuts import render

# Create your views here.
def first_2(request):
    return render(request,'third.html')
def second_2(request):
    return render(request,'fourth.html')
