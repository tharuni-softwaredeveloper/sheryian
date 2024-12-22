from django.shortcuts import render

# Create your views here.
def bootcamp(request):
    return render(request,'bootcamp.html')