from django.shortcuts import render

# Create your views here.
def recruit(request):
    return render(request, "recruit/recruit.html")