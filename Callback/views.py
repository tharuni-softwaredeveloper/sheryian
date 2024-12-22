from django.shortcuts import render

# Create your views here.
def callback(request):
    return render(request,'callback.html')
